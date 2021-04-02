import socket
import logging
import json
from jog_wheel import JogWheel
from socket_client import CommandTransmitter

class JogWithSpeed:

    def __init__(self, log_level=logging.INFO) -> None:
        self.jog_wheel = JogWheel(callback=self.callback, log_level=logging.INFO)
        self.transmitter = CommandTransmitter.get_instance()
        self.setup_logging(log_level)

    def setup_logging(self, log_level):
        logging.basicConfig(format="%(asctime)s [%(levelname)s] %(name)s: [%(threadName)s] %(message)s ")
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(log_level)

    def callback(self, direction=None, speed=None):
        increment = self.get_increment(speed)
        increment = increment if direction == JogWheel.RIGHT else - increment
        self.logger.debug(f"inc={increment} speed={speed}")
        self.transmitter.change_position(increment)

    def get_increment(self, speed):
        if not speed:
            return .001
        elif speed < 50:
            return .001
        elif speed < 100:
            return .01
        else:
            return .05


if __name__ == '__main__':
    j = JogWithSpeed(log_level=logging.DEBUG)
    pass
