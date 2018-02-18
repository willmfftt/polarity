import logging
import os
import sys

import argparse

from polarity.bruteforce import BruteforceFactory
from polarity.enumeration import UserEnumerator
from polarity.network_scanner import PortScan
from polarity.objects import User


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--network", "-n", required=True,
                        help="Target network to attack")
    parser.add_argument("--users", "-U", required=False,
                        help="File containing a user list")
    parser.add_argument("--user", "-u", required=False,
                        help="Single user to use during attacks")
    parser.add_argument("--passwords", "-P", required=False,
                        help="File containing a password list")
    parser.add_argument("--password", "-p", required=False,
                        help="Single password to use during attacks")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(os.EX_SOFTWARE)

    logging.basicConfig(level=logging.INFO)

    args = parser.parse_args()

    user_set = set()
    password_set = set()
    single_user = None

    if args.user and not args.password:
        logging.error("A password must be specified for user")
        sys.exit(os.EX_SOFTWARE)
    elif args.password and not args.user:
        logging.error("A user must be specified with a password")
        sys.exit(os.EX_SOFTWARE)
    elif args.user and args.password:
        single_user = User()
        single_user.username = args.user
        single_user.password = args.password

    if not single_user:
        if not args.passwords:
            logging.error("If no user and password is specified, "
                          "a password list must be given")
            sys.exit(os.EX_SOFTWARE)

    if args.users:
        if not os.path.isfile(args.users):
            logging.error("Supplied user list is invalid")
            sys.exit(os.EX_SOFTWARE)

        with open(args.users, 'r') as users_file:
            for user in users_file.readlines():
                user_set.add(user.strip())

    if args.passwords:
        if not os.path.isfile(args.passwords):
            logging.error("Supplied password list is invalid")
            sys.exit(os.EX_SOFTWARE)

        with open(args.passwords, 'r') as passwords_file:
            for password in passwords_file.readlines():
                password_set.add(password.strip())

    hosts = PortScan.start_scan(args.network)

    if not single_user:
        for host in hosts:
            enumerator = UserEnumerator(host)
            users = enumerator.enumerate()
            if users:
                host.users = users
                for user in users:
                    user_set.add(user.username)

            bruteforcers = (BruteforceFactory
                            .get_bruteforcers_for_host(host, list(user_set),
                                                       list(password_set)))
            for bruteforcer in bruteforcers:
                results = bruteforcer.start_bruteforce()
                if results:
                    for username in results.keys():
                        user = host.get_user_by_username(username)
                        if user:
                            user.password = results[username]
                    break

    sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()
