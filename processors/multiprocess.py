import logging
import multiprocessing
from multiprocessing import Pool
from typing import List

from pingers.factory import PingerFactory
from pingresult import PingResult
from processor import PingProcessor


class MultiProcessPingProcessor(PingProcessor):
    processes: int

    def __init__(self, processes: int):
        self.processes = processes
        if processes > multiprocessing.cpu_count():
            logging.warning(f'Input pool size {processes} is greater than cpu count {multiprocessing.cpu_count()}.'
                            f' Using cpu count instead.')
            self.processes = multiprocessing.cpu_count()

    def do_ping_job(self, hosts: List[str], iterations: float) -> List[PingResult]:
        with Pool(self.processes) as pool:
            ping_args = list()
            for host in hosts:
                ping_args.append((host, iterations))
            results = pool.starmap(self._job_function, ping_args)
        pool.close()
        pool.join()
        return results

    @staticmethod
    def _job_function(host: str, iterations: float) -> PingResult:
        pinger = PingerFactory().get_system_pinger()
        return pinger.ping(host, int(iterations))
