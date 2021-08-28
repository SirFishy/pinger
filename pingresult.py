from dataclasses import dataclass


@dataclass
class PingResult:
    host: str
    total_ping_time: float

    def __init__(self, host: str, total_ping_time: float):
        self.host = host
        self.total_ping_time = total_ping_time
