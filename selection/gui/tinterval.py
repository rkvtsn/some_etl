#github.com/rkvtsn
import threading


class TimeInterval(object):
    """ JS-like setInterval """
    def __init__(self, timeout, fn):
        """
        :param timeout: timeout in seconds
        :param fn: function
        """
        self.t = None
        self.fn = fn
        self.timeout = timeout
        self._is_running = False

    def start(self):
        """Launch interval with init params"""
        if self._is_running:
            return
        def func_wrapper():
            timeout = self.fn()
            if timeout is not None:
                self.timeout = timeout
            self._is_running = False
            self.start()
        self.t = threading.Timer(self.timeout, func_wrapper)
        self.t.start()
        self._is_running = True

    def stop(self):
        """Stop interval"""
        if not self._is_running:
            return
        self._is_running = False
        self.t.cancel()

    def set_timeout(self, timeout):
        """Restart interval, reset timeout and launch"""
        self.timeout = timeout
        self.stop()
        self.start()
