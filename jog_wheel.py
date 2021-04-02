import RPi.GPIO as GPIO
import time
import logging
from collections import deque
from statistics import mean

class JogWheel:
    RIGHT_PIN = 17
    LEFT_PIN = 27
    INPUTS = [RIGHT_PIN, LEFT_PIN]
    RIGHT = 0
    LEFT = 1

    def __init__(self, callback=None) -> None:
        self.setup_logging()
        self.callback = callback
        self.setup_gpio()
        self.last_event_time = time.monotonic()
        self.reset_speed_q()

    def setup_logging(self ):
        self.logger = logging.getLogger()
        self.logger.name = self.__class__.__name__
        self.logger.info('test')

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__class__.INPUTS, GPIO.IN)
        GPIO.add_event_detect(self.__class__.RIGHT_PIN, GPIO.RISING)
        GPIO.add_event_callback(self.__class__.RIGHT_PIN, self.right)
        GPIO.add_event_detect(self.__class__.LEFT_PIN, GPIO.RISING)
        GPIO.add_event_callback(self.__class__.LEFT_PIN, self.left)

    def right(self, channel):
        speed = self.get_speed()
        self.speed_q.appendleft(speed)
        self.logger.debug(f"direction=right speed={speed}")
        self.callback and self.callback(direction=self.__class__.RIGHT, speed=speed)

    def left(self, channel):
        speed = self.get_speed()
        self.logger.debug(f"direction=left speed={speed}")
        self.callback and self.callback(direction=self.__class__.LEFT, speed=speed)

    def get_speed(self):
        now = time.monotonic()
        time_lapse = now - self.last_event_time
        self.last_event_time = now
        speed = 1.0 / time_lapse
        if speed < 5:
            self.reset_speed_q()
        else:
            self.speed_q.appendleft(speed)
        return mean(self.speed_q)

    def reset_speed_q(self):
        self.speed_q = deque(5*[0], 5)