from polarity.objects.port import Port
from polarity.objects.os_info import OSInfo
from polarity.utils import NmapParser


class Host:

    def __init__(self, ip_address=None):
        self._ip_address = ip_address

        self._ports = []
        self._os_info = None
        self._users = []

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        self._ip_address = ip_address

    @property
    def ports(self):
        return self._ports

    @ports.setter
    def ports(self, ports):
        self._ports = ports

    def add_port(self, port):
        self._ports.append(port)

    @property
    def os_info(self):
        return self._os_info

    @os_info.setter
    def os_info(self, os_info):
        self._os_info = os_info

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users):
        self._users = users

    def add_user(self, user):
        self._users.append(user)

    def get_user_by_username(self, username):
        for user in self._users:
            if username == user.username:
                return user
        return None

    @staticmethod
    def build(nmap_host):
        parser = NmapParser(nmap_host)
        host = Host()

        if not parser.ip_address:
            return None
        host.ip_address = parser.ip_address

        for port_number in parser.tcp_port_numbers:
            port = Port.build(port_number, "tcp", parser)
            if port:
                host.add_port(port)

        for port_number in parser.udp_port_numbers:
            port = Port.build(port_number, "udp", parser)
            if port:
                host.add_port(port)

        os_info = OSInfo.build(parser)
        host.os_info = os_info

        return host
