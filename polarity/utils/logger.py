import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


class Logger:

    ERROR = 0
    INFO = 1
    DEBUG = 2

    def __init__(self, log_level=INFO):
        self._log_level = log_level

    def log(self, level, msg):
        if level <= self._log_level:
            print(msg)
