import concurrent
from typing import List

from pingers.windows import WindowsPinger
from pingresult import PingResult
from processor import PingProcessor


class MultiThreadPingProcessor(PingProcessor):
    pools: int

    def __init__(self, pools: int, ):
        self.pools = pools

    def do_ping_job(self, hosts: List[str], iterations: float) -> List[PingResult]:
        future_results = list()
        with concurrent.futures.ThreadPoolExecutor(self.pools) as executor:
            for host in hosts:
                pinger = WindowsPinger()
                future_results.append(executor.submit(pinger.timed_ping, host, iterations))
        ping_results = list()
        for result in future_results:
            ping_results.append(result.result())
        return ping_results