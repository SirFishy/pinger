import argparse
import json
import time
import concurrent.futures
from typing import List
from pingers.windows import WindowsPinger


def read_hosts() -> List[str]:
    with open('data.json') as file_handle:
        json_data = json.load(file_handle)
        return json_data["hosts"]


def time_ping_host(host: str, iterations: int) -> float:
    host_pinger = WindowsPinger()
    return host_pinger.timed_ping(host, iterations)


def do_ping_job(args: argparse.Namespace):
    future_results = list()
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(args.pool) as executor:
        for host in read_hosts():
            future_results.append(executor.submit(time_ping_host, host, args.iterations))
    max_ping = 0
    for result in future_results:
        max_ping = max(max_ping, result.result())
    print(f"Longest job took {max_ping} seconds to run")
    print(f"Program took {time.time() - start_time} seconds to run")


def check_positive(value):
    try:
        int_value = int(value)
    except ValueError:
        raise argparse.ArgumentError(f"{value} should be an integer")

    if int_value <= 0:
        raise argparse.ArgumentTypeError(f"Invalid input: {value}, should be greater than 0")
    return int_value


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ping some websites.')
    parser.add_argument('--pool', type=check_positive, help='Number of pools for executor', default=5)
    parser.add_argument('--iterations', type=check_positive, help='Number of times to ping each website', default=5)
    do_ping_job(parser.parse_args())

