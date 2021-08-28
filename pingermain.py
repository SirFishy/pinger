import argparse
import json
import time
from typing import List
from processors.multithread import MultiThreadPingProcessor


def read_hosts() -> List[str]:
    with open('data.json') as file_handle:
        json_data = json.load(file_handle)
        try:
            hosts = json_data["hosts"]
        except KeyError as err:
            raise Exception("The list of `hosts' could not be parsed from data.json")
        return hosts


def do_ping_job(args: argparse.Namespace):
    start_time = time.time()
    processor = MultiThreadPingProcessor(args.pool)
    hosts = read_hosts()
    if len(hosts) < 1:
        raise Exception("data.json did not contain any hosts to ping.")
    ping_results = processor.do_ping_job(hosts, args.iterations)
    max_ping = 0
    max_host = ""
    for result in ping_results:
        prev_ping = max_ping
        max_ping = max(max_ping, result.total_ping_time)
        if prev_ping != max_ping:
            max_host = result.host
    print(f"Longest job took {max_ping} seconds to ping {max_host}")
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

