import subprocess

from pinger import Pinger


class UnixPinger(Pinger):

    @Pinger.log_ping_decorator
    def _subprocess_ping(self, host: str, iterations: int):
        ping_process = subprocess.Popen(["ping", "-c", f"{iterations}", host], stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, text=True)
        return ping_process.communicate()
