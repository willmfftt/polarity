from polarity.bruteforce.ftp_bruteforce import FTPBruteforce
from polarity.bruteforce.smb_bruteforce import SMBBruteforce
from polarity.bruteforce.ssh_bruteforce import SSHBruteforce


class BruteforceFactory:

    PRIORITIZED_PORTS = [
        SMBBruteforce.PORT,
        FTPBruteforce.PORT,
        SSHBruteforce.PORT,
    ]

    @classmethod
    def get_bruteforcers_for_host(cls, host, users, passwords):
        port_numbers = []
        prioritized_bruteforcers = []

        for port in host.ports:
            port_numbers.append(port.port)

        for prioritized_port in cls.PRIORITIZED_PORTS:
            if prioritized_port in port_numbers:
                prioritized_bruteforcers.append(
                    cls.get_bruteforce(prioritized_port, host,
                                       users, passwords)
                )

        return prioritized_bruteforcers

    @staticmethod
    def get_bruteforce(port, host, users, passwords):
        if port == FTPBruteforce.PORT:
            return FTPBruteforce(host, users, passwords)
        elif port == SMBBruteforce.PORT:
            return SMBBruteforce(host, users, passwords)
        elif port == SSHBruteforce.PORT:
            return SSHBruteforce(host, users, passwords)
        else:
            return None
