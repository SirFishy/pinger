from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from pingresult import PingResult


class ProcessorType(Enum):
    PROCESS = "process"
    THREAD = "thread"


class PingProcessor(ABC):

    @abstractmethod
    def do_ping_job(self, hosts: List[str], iterations: float) -> List[PingResult]:
        pass
