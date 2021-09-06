import sys
import logging
from pinger import Pinger
from pingers.unix import UnixPinger
from pingers.windows import WindowsPinger


class PingerFactory:

    def get_system_pinger(self) -> Pinger:
        pinger = None
        if sys.platform.startswith('freebsd') or sys.platform.startswith('linux') or sys.platform.startswith('aix') \
                or sys.platform.startswith('darwin'):
            pinger = UnixPinger()
        elif sys.platform.startswith('win32'):
            pinger = WindowsPinger()
        elif sys.platform.startswith('cygwin'):
            raise NotImplementedError(self._get_exception_message('cygwin'))
        logging.debug(f"Creating {pinger.__class__.__name__} for {sys.platform}")
        return pinger

    @staticmethod
    def _get_exception_message(platform_uname) -> str:
        return f"Platform with uname {platform_uname} is not supported."
