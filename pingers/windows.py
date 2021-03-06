import subprocess

from pinger import Pinger


class WindowsPinger(Pinger):

    @Pinger.log_ping_decorator
    def _subprocess_ping(self, host: str, iterations: int):
        ping_process = subprocess.Popen(["ping", "-n", f"{iterations}", host], stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, text=True)
        return ping_process.communicate()
