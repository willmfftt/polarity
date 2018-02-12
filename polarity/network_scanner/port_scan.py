import multiprocessing

from multiprocessing.dummy import Pool as ThreadPool
from polarity.utils import Logger
from scapy.all import *


class PortScan:

    _PORT_RANGE = list(range(1, 1000))
    _TIMEOUT = 0.2

    def __init__(self, host, port_range=_PORT_RANGE):
        self._host = host
        self._port_range = port_range
        self.logger = Logger()

    def start_tcp_scan(self):
        self.logger.log(Logger.INFO, "Starting tcp port scan on host {}"
                        .format(str(self._host)))

        pool = ThreadPool(multiprocessing.cpu_count() * 2)
        open_ports = pool.map(self.scan_tcp_port, self._port_range)

        return list(filter(None, open_ports))

    def scan_tcp_port(self, port):
        scan_pkt = (IP(dst=str(self._host))/
                    TCP(dport=port, flags="S"))

        resp_pkt = sr1(scan_pkt, timeout=self._TIMEOUT, verbose=False)
        if resp_pkt and resp_pkt.haslayer(TCP):
            if resp_pkt[TCP].flags == 18:
                self.logger.log(Logger.INFO, "[{}] tcp port {} is open"
                                .format(str(self._host), str(port)))
                return port

        return None

    def start_udp_scan(self):
        self.logger.log(Logger.INFO, "Starting udp port scan on host {}"
                        .format(str(self._host)))

        pool = ThreadPool(multiprocessing.cpu_count() * 2)
        open_ports = pool.map(self.scan_udp_port, self._port_range)

        return list(filter(None, open_ports))

    def scan_udp_port(self, port):
        scan_pkt = IP(dst=str(self._host))/UDP(dport=port)

        resp_pkt = sr1(scan_pkt, timeout=self._TIMEOUT, verbose=False)
        if resp_pkt and resp_pkt.haslayer(UDP):
            self.logger.log(Logger.INFO, "[{}] udp port {} is open"
                            .format(str(self._host), str(port)))
            return port

        return None
