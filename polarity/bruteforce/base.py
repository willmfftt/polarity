class BaseBruteforce:

    PORT = 0

    def __init__(self, host, users, passwords):
        self._host = host
        self._users = users
        self._passwords = passwords

    def start_bruteforce(self):
        raise NotImplementedError
