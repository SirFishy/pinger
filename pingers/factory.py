import sys
from pinger import Pinger
from pingers.unix import UnixPinger
from pingers.windows import WindowsPinger


class PingerFactory:

    def get_system_pinger(self)-> Pinger:
        if sys.platform.startswith('freebsd') or sys.platform.startswith('linux') or sys.platform.startswith('aix') \
                or sys.platform.startswith('darwin'):
            return UnixPinger()
        elif sys.platform.startswith('win32'):
            return WindowsPinger()
        elif sys.platform.startswith('cygwin'):
            raise NotImplementedError(self._get_exception_message('cygwin'))

    @staticmethod
    def _get_exception_message(platform_uname) -> str:
        return f"Platform with uname {platform_uname} is not supported."
