import subprocess

from pinger import Pinger


class WindowsPinger(Pinger):

    def ping(self, host: str, iterations: int):
        ping_process = subprocess.Popen(["ping", "-n", f"{iterations}", host], stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, text=True)
        pipe_data = ping_process.communicate()
        for data in pipe_data:
            self.safe_print(str(data))
