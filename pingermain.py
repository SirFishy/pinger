import argparse
import json
import logging
import time
from typing import List

from processor import ProcessorType
from processors.factory import ProcessorFactory


def read_hosts() -> List[str]:
    with open('data.json') as file_handle:
        json_data = json.load(file_handle)
        try:
            hosts = json_data["hosts"]
            logging.debug(f"Parsed {hosts}")
        except KeyError as err:
            logging.error("The list of 'hosts' could not be parsed from data.json")
            raise Exception(err)
        if len(hosts) < 1:
            err_msg = "data.json did not contain any hosts to ping."
            logging.error(err_msg)
            raise Exception(err_msg)
        return hosts


def do_ping_job(args: argparse.Namespace):
    start_time = time.time()
    processor = ProcessorFactory().get_processor(ProcessorType(args.processor), args.parallel)
    hosts = read_hosts()
    ping_results = processor.do_ping_job(hosts, args.iterations)
    max_ping = 0
    max_host = ""
    for result in ping_results:
        prev_ping = max_ping
        max_ping = max(max_ping, result.total_ping_time)
        if prev_ping != max_ping:
            max_host = result.host
    logging.info(f"Longest job took {max_ping} seconds to ping {max_host}")
    logging.info(f"Program took {time.time() - start_time} seconds to run")


def check_positive(value):
    try:
        int_value = int(value)
    except ValueError:
        raise argparse.ArgumentError(None, f"{value} should be an integer")

    if int_value <= 0:
        raise argparse.ArgumentTypeError(None, f"Invalid input: {value}, should be greater than 0")
    return int_value


def check_processor(value):
    if value not in set(item.value for item in ProcessorType):
        raise argparse.ArgumentError(f"{value} is not a valid processor.")
    return value


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(relativeCreated)6d %(threadName)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    parser = argparse.ArgumentParser(description='Ping some websites.')
    parser.add_argument('--parallel', type=check_positive, help='Number of jobs to run in parallel', default=5)
    parser.add_argument('--iterations', type=check_positive, help='Number of times to ping each website', default=5)
    parser.add_argument('--processor', type=check_processor, choices=[item.value for item in ProcessorType],
                        help='Parallel processor implementation.', default='thread')
    parsed_args = parser.parse_args()
    logging.info(f"Number of parallel jobs: {parsed_args.parallel}")
    logging.info(f"Number of ping iterations: {parsed_args.iterations}")
    logging.info(f"Processor implementation: {ProcessorType(parsed_args.processor)}")
    do_ping_job(parsed_args)

