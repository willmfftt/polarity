import logging
import re
import shutil
import subprocess


class RpcClient:

    @classmethod
    def enumerate_users(cls, host, workgroup):
        rpcclient = shutil.which("rpcclient")
        if not rpcclient:
            logging.warning("rpcclient not installed, aborting user enumeration")
            return []

        command = [
            rpcclient,
            "-W",
            workgroup,
            "-c",
            "querydispinfo",
            "-U",
            "",
            "-N",
            host.ip_address
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE)

        parser = cls.Parser(result.stdout.decode("utf-8"))

        return parser.get_users()

    class Parser:

        def __init__(self, data):
            self._data = data

        def get_users(self):
            p = re.compile("(?<=acb: 0x00000010 Account: )(.*)(?=\tName)")
            return p.findall(self._data)
