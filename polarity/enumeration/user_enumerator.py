import logging

from nmb.NetBIOS import NetBIOS

from polarity.enumeration.rpc_client import RpcClient
from polarity.objects import User


class UserEnumerator:

    def __init__(self, host):
        self._host = host

    def enumerate(self):
        users = set()

        logging.info("Starting user enumeration for host: %s",
                     self._host.ip_address)

        workgroups = self.__get_workgroups()

        if not workgroups:
            logging.info("No workgroups found")
            return []

        logging.info("Workgroups found, enumerating users")
        for workgroup in workgroups:
            tmp_users = RpcClient.enumerate_users(self._host, workgroup)
            for username in tmp_users:
                users.add(User(username))

        return list(users)

    def __get_workgroups(self):
        logging.info("Enumerating workgroups")
        netbios = NetBIOS(broadcast=False)
        return netbios.queryIPForName(self._host.ip_address,
                                      timeout=0.5)
