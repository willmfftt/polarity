class NmapParser:

    def __init__(self, data):
        self._data = data

    @property
    def addresses(self):
        if "addresses" in self._data:
            return self._data["addresses"]
        return {}

    @property
    def ip_address(self):
        return self.addresses.get("ipv4")

    @property
    def tcp_port_numbers(self):
        return self._data.all_tcp()

    @property
    def udp_port_numbers(self):
        return self._data.all_udp()

    def get_port_data(self, port):
        if self.is_port_open(port):
            return self._data.tcp(port)
        return {}

    def get_service_name(self, port):
        return self.get_port_data(port).get("name")

    def get_service_vendor(self, port):
        return self.get_port_data(port).get("product")

    def get_service_version(self, port):
        return self.get_port_data(port).get("version")

    def get_service_extra(self, port):
        return self.get_port_data(port).get("extrainfo")

    def is_port_open(self, port):
        if self._data.has_tcp(port):
            return self._data.tcp(port).get("state") == "open"
        return False

    def get_os_data(self):
        if "osmatch" in self._data:
            if len(self._data.get("osmatch")) > 0:
                return self._data.get("osmatch")[0]
        return {}

    def get_os_class(self):
        if "osclass" in self.get_os_data():
            if len(self.get_os_data().get("osclass")) > 0:
                return self.get_os_data().get("osclass")[0]
        return {}

    @property
    def os_name(self):
        return self.get_os_data().get("name")

    @property
    def os_type(self):
        return self.get_os_class().get("type")

    @property
    def os_vendor(self):
        return self.get_os_class().get("vendor")

    @property
    def os_family(self):
        return self.get_os_class().get("osfamily")

    @property
    def os_gen(self):
        return self.get_os_class().get("osgen")