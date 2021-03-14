import RPi.GPIO as GPIO
import time
import logging

class JogWheel:
    RIGHT_PIN = 17
    LEFT_PIN = 27
    INPUTS = [RIGHT_PIN, LEFT_PIN]
    RIGHT = 0
    LEFT = 1

    def __init__(self, callback=None, log_level=logging.DEBUG) -> None:
        self.callback = callback
        self.setup_logging(log_level)
        self.setup_gpio()
        self.last_event_time = time.monotonic()

    def setup_logging(self, log_level):
        logging.basicConfig(format="%(asctime)s [%(levelname)s] %(name)s: [%(threadName)s] %(message)s ")
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(log_level)

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__class__.INPUTS, GPIO.IN)
        GPIO.add_event_detect(self.__class__.RIGHT_PIN, GPIO.RISING)
        GPIO.add_event_callback(self.__class__.RIGHT_PIN, self.right)
        GPIO.add_event_detect(self.__class__.LEFT_PIN, GPIO.RISING)
        GPIO.add_event_callback(self.__class__.LEFT_PIN, self.left)

    def right(self, channel):
        speed = self.get_speed()
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
        return 1.0 / time_lapse

if __name__ == '__main__':
    j = JogWheel()



pass