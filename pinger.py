import time
from abc import ABC, abstractmethod
from globalthread import print_lock


class Pinger(ABC):

    @abstractmethod
    def ping(self, host: str, iterations: int):
        pass

    def timed_ping(self, host: str, iterations: int) -> float:
        start_time = time.time()
        self.ping(host, iterations)
        return time.time() - start_time

    @staticmethod
    def safe_print(*args, **kwargs):
        with print_lock:
            print(*args, **kwargs)
