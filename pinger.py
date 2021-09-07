import time
import logging
from abc import ABC, abstractmethod
from functools import wraps
from typing import Tuple, AnyStr

from globalthread import print_lock
from pingresult import PingResult


class Pinger(ABC):

    @abstractmethod
    def _subprocess_ping(self, host: str, iterations: int) -> Tuple[AnyStr, AnyStr]:
        pass

    def ping(self, host: str, iterations: int) -> PingResult:
        start_time = time.time()
        self._subprocess_ping(host, iterations)
        return PingResult(host, time.time() - start_time)

    @staticmethod
    def safe_print(*args, **kwargs):
        with print_lock:
            print(*args, **kwargs)

    @staticmethod
    def log_ping_decorator(subprocess_ping_func):
        @wraps(subprocess_ping_func)
        def wrapper(*args, **kwargs):
            logging.info(f"Pinging {args[1]} {args[2]} times.")
            stdout, stderr = subprocess_ping_func(*args, **kwargs)
            if stdout:
                logging.info(stdout)
            if stderr:
                logging.info(stderr)
            return stdout, stderr
        return wrapper





