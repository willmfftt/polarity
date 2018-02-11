import multiprocessing

from multiprocessing.dummy import Pool as ThreadPool
from polarity.utils import Logger
from scapy.all import *


class QuickScan:

    _PORT_RANGE = list(range(1, 1000))
    _TIMEOUT = 0.2

    def __init__(self, host, port_range=_PORT_RANGE):
        self._host = host
        self._port_range = port_range
        self.logger = Logger()

    def start_scan(self):
        self.logger.log(Logger.INFO, "Starting port scan on host {}"
                        .format(str(self._host)))

        pool = ThreadPool(multiprocessing.cpu_count() * 2)
        open_ports = pool.map(self.scan_port, self._port_range)

        return list(filter(None, open_ports))

    def scan_port(self, port):
        scan_pkt = (IP(dst=str(self._host))/
                    TCP(dport=port, flags="S"))

        resp_pkt = sr1(scan_pkt, timeout=self._TIMEOUT, verbose=False)
        if resp_pkt:
            if resp_pkt[TCP].flags == 18:
                self.logger.log(Logger.INFO, "[{}] port {} is open"
                                .format(str(self._host), str(port)))
                return port

        return None
