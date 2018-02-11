import multiprocessing

from polarity.utils import Logger
from scapy.all import *
from multiprocessing.dummy import Pool as ThreadPool


class PingScan:

    _TIMEOUT = 0.5

    @staticmethod
    def start_scan(network):
        logger = Logger()
        logger.log(Logger.INFO, "Starting ping scan against {}"
                   .format(str(network)))

        pool = ThreadPool(multiprocessing.cpu_count() * 2)
        alive_hosts = pool.map(PingScan.ping_host, network.hosts())

        return list(filter(None, alive_hosts))

    @classmethod
    def ping_host(cls, host):
        logger = Logger()
        ping_pkt = IP(dst=str(host))/ICMP()

        resp_pkt = sr1(ping_pkt, timeout=cls._TIMEOUT, verbose=False)
        if resp_pkt:
            logger.log(Logger.INFO, "Host {} is up".format(str(host)))
            return host

        return None
