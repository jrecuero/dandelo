"""itimer.py module contains all functionality required for engine timers.
"""

from ssl import AlertDescription
from . import iobject

ALWAYS_TIME = -1
ONE_TIME = 1

class ITimer(iobject.IObject):
    """ITimer class contains all functionality to create an engine timer.
    """

    def __init__(self, a_name, a_timeout, a_callback, a_cb_args=None, a_time=ALWAYS_TIME):
        """__init__ method creates a new ITimer instance.

        = a_name attribute contains the name for the timer.

        - timeout attribute contains the timeout of the timer will expire in
        milliseconds.

        - timeout_counter attribute contains the internal counter with the
        number of milliseconds passed from the last time the timer expired.

        - times attributes contains the number of times the timer will be
        repeated. If value is ALWAYS_TIME=0, it will repeated indefinitely.

        - callback attribute contains the function to be called when the timer
        expires.

        - callback_args attribute contains the dictionary with parameter to be
        passed to the timer callback.
        """
        super().__init__(a_name)
        self.timeout = a_timeout
        self.timeout_counter = 0
        self.times = a_time
        self.callback = a_callback
        self.callback_args = a_cb_args

    def tick(self, a_fps):
        """tick method adds a new tick time to the timer and check if it has
        expired.
        """
        if self.times == 0:
            return False
        v_timeout = 1000 / a_fps
        self.timeout_counter += v_timeout
        if self.timeout_counter >= self.timeout:
            self.timeout_counter = 0
            # TODO: Create an event instead of a direct call.
            self.callback(self.callback_args)
            if self.times != ALWAYS_TIME:
                self.times -= 1
        return True
