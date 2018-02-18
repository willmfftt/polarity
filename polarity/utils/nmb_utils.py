from nmb.NetBIOS import NetBIOS


class NMBUtils:

    @staticmethod
    def get_workgroups(host):
        netbios = NetBIOS(broadcast=False)
        workgroups = netbios.queryIPForName(host.ip_address,
                                            timeout=0.5)
        return workgroups if workgroups else []
