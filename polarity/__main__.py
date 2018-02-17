import logging
import os
import sys

import argparse

from polarity.network_scanner import PortScan


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

    hosts = PortScan.start_scan(args.network)

    sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()
