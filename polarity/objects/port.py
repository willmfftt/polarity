from polarity.objects.service_info import ServiceInfo


class Port:

    def __init__(self, port=None, protocol=None):
        self._port = port
        self._protocol = protocol

        self._service_info = None

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        self._protocol = protocol

    @property
    def service_info(self):
        return self._service_info

    @service_info.setter
    def service_info(self, service_info):
        self._service_info = service_info

    @staticmethod
    def build(port_number, protocol, parser):
        port = Port()

        port.port = port_number
        port.protocol = protocol

        service_info = ServiceInfo.build(port_number, parser)
        port.service_info = service_info

        return port
