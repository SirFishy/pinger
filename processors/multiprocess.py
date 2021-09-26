import concurrent.futures
from multiprocessing import Pool
from typing import List

from pingers.factory import PingerFactory
from pingresult import PingResult
from processor import PingProcessor


class MultiProcessPingProcessor(PingProcessor):
    processes: int

    def __init__(self, processes: int):
        self.processes = processes

    def do_ping_job(self, hosts: List[str], iterations: float) -> List[PingResult]:
        with Pool(self.processes) as pool:
            ping_args = list()
            for host in hosts:
                ping_args.append((host, iterations))
            results = pool.starmap(self._job_function, ping_args)
        pool.close()
        pool.join()
        return results

    def _job_function(self, host: str, iterations: float) -> PingResult:
        pinger = PingerFactory().get_system_pinger()
        return pinger.ping(host, int(iterations))
