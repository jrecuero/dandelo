"""itimer.py module contains all functionality required for engine timers.
"""

import pygame
from . import iobject

ALWAYS_TIME = -1
ONE_TIME = 1

class Timer(iobject.IObject):
    """Timer class contains all functionality to create an engine timer.
    """

    def __init__(self, a_name, a_timeout, a_callback, a_cb_args={}, a_time=ONE_TIME):
        """__init__ method creates a new Timer instance.

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
        self.start_time = 0
        self.times = a_time
        self.callback = a_callback
        self.callback_args = a_cb_args
        self.active = False

    def activate(self):
        """activate method activates the timer.
        """
        self.activate = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        """deactivate method deactivates the timer.
        """
        self.activate = False
        self.start_time = 0

    def tick(self):
        """tick method adds a new tick time to the timer and check if it has
        expired.
        """
        if not self.activate:
            return False
        v_actual_time = pygame.time.get_ticks()
        if v_actual_time - self.start_time >= self.timeout:
            self.callback(**self.callback_args)
            self.start_time = v_actual_time 
            if self.times != ALWAYS_TIME:
                self.times -= 1
            if self.times == 0:
                self.deactivate()
        return True
