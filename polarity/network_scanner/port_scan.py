import logging

from nmap import PortScanner
from nmap import PortScannerError

from polarity.objects import Host


class PortScan:

    @classmethod
    def start_scan(cls, network):
        hosts_found = []

        logging.info("Starting scan on network: %s", str(network))

        try:
            nmap = PortScanner()
            nmap.scan(str(network), '1-1000', '-sV -O', True)
        except PortScannerError as err:
            logging.error("Scan failed: %s", err)
            return hosts_found

        for host in nmap.all_hosts():
            if nmap[host].state() == "up":
                hosts_found.append(Host.build(nmap[host]))

        return hosts_found
