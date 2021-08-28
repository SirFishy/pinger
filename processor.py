from abc import ABC, abstractmethod
from typing import List

from pingresult import PingResult


class PingProcessor(ABC):

    @abstractmethod
    def do_ping_job(self, hosts: List[str], iterations: float) -> List[PingResult]:
        pass
