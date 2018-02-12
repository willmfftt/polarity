class Port:

    TCP = "tcp"
    UDP = "udp"

    def __init__(self, port, protocol):
        self._port = port
        self._protocol = protocol

    @property
    def port(self):
        return self._port

    @property
    def protocol(self):
        return self._protocol

    def __str__(self):
        return "{}/{}".format(str(self.port), self.protocol)
