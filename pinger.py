import time
from abc import ABC, abstractmethod
from globalthread import print_lock
from pingresult import PingResult


class Pinger(ABC):

    @abstractmethod
    def ping(self, host: str, iterations: int):
        pass

    def timed_ping(self, host: str, iterations: int) -> PingResult:
        start_time = time.time()
        self.ping(host, iterations)
        return PingResult(host, time.time() - start_time)

    @staticmethod
    def safe_print(*args, **kwargs):
        with print_lock:
            print(*args, **kwargs)
