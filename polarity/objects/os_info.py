class OSInfo:

    def __init__(self):
        self._os_name = None
        self._os_type = None
        self._os_vendor = None
        self._os_family = None
        self._os_gen = None

    @property
    def os_name(self):
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        self._os_name = os_name

    @property
    def os_type(self):
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        self._os_type = os_type

    @property
    def os_vendor(self):
        return self._os_vendor

    @os_vendor.setter
    def os_vendor(self, os_vendor):
        self._os_vendor = os_vendor

    @property
    def os_family(self):
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        self._os_family = os_family

    @property
    def os_gen(self):
        return self._os_gen

    @os_gen.setter
    def os_gen(self, os_gen):
        self._os_gen = os_gen

    @staticmethod
    def build(parser):
        os_info = OSInfo()

        os_info.os_name = parser.os_name
        os_info.os_type = parser.os_type
        os_info.os_vendor = parser.os_vendor
        os_info.os_family = parser.os_family
        os_info.os_gen = parser.os_gen

        return os_info
