class ServiceInfo:

    def __init__(self):
        self._service_name = None
        self._service_vendor = None
        self._service_version = None
        self._extras = None

    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        self._service_name = service_name

    @property
    def service_vendor(self):
        return self._service_vendor

    @service_vendor.setter
    def service_vendor(self, service_vendor):
        self._service_vendor = service_vendor

    @property
    def service_version(self):
        return self._service_version

    @service_version.setter
    def service_version(self, service_version):
        self._service_version = service_version

    @property
    def extras(self):
        return self._extras

    @extras.setter
    def extras(self, extras):
        self._extras = extras

    @staticmethod
    def build(port_number, parser):
        service_info = ServiceInfo()

        service_info.service_name = parser.get_service_name(port_number)
        service_info.service_vendor = parser.get_service_vendor(port_number)
        service_info.service_version = parser.get_service_version(port_number)
        service_info.extras = parser.get_service_extra(port_number)

        return service_info
