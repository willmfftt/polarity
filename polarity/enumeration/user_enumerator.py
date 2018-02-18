import logging

from polarity.enumeration.rpc_client import RpcClient
from polarity.objects import User
from polarity.utils import NMBUtils


class UserEnumerator:

    def __init__(self, host):
        self._host = host

    def enumerate(self):
        users = set()

        logging.info("Starting user enumeration for host: %s",
                     self._host.ip_address)

        workgroups = NMBUtils.get_workgroups(self._host)

        for workgroup in workgroups:
            tmp_users = RpcClient.enumerate_users(self._host, workgroup)
            for username in tmp_users:
                users.add(User(username))

        logging.info("Found %d users", len(users))

        return list(users)
