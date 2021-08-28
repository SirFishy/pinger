import time

from pingers.windows import WindowsPinger
import concurrent.futures


def time_ping_google(iterations: int) -> float:
    google_pinger = WindowsPinger()
    return google_pinger.timed_ping("www.google.com", iterations)


def time_ping_yahoo(iterations: int) -> float:
    yahoo_pinger = WindowsPinger()
    return yahoo_pinger.timed_ping("www.yahoo.com", iterations)


def time_ping_stackoverflow(iterations: int) -> float:
    stackoverflow_pinger = WindowsPinger()
    return stackoverflow_pinger.timed_ping("www.stackoverflow.com", iterations)


def time_ping_twitch(iterations: int) -> float:
    twitch_pinger = WindowsPinger()
    return twitch_pinger.timed_ping("www.twitch.com", iterations)


if __name__ == '__main__':
    pool_size = 5
    iterations = 5
    future_results = list()
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(pool_size) as executor:
        future_results.append(executor.submit(time_ping_google, iterations))
        future_results.append(executor.submit(time_ping_yahoo, iterations))
        future_results.append(executor.submit(time_ping_stackoverflow, iterations))
        future_results.append(executor.submit(time_ping_twitch, iterations))
    max_ping = 0
    for result in future_results:
        max_ping = max(max_ping, result.result())
    print(f"Longest job took {max_ping} seconds to run")
    print(f"Program took {time.time() - start_time} seconds to run")
