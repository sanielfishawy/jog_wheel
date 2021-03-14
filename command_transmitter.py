import requests
import urllib3
import logging
import socketio

class Commands:
    SAVE_POSITION= 'save_position'
    CHANGE_POSITION= 'change_position'

class ParameterKeys:
    COMMAND_KEY = 'command'
    POSITION_KEY = 'position'

class Transmitter:
    PATH = 'http://10.0.0.102:5005'

    def __init__(self) -> None:
        self.sio = socketio.Client()
        self.sio.connect(self.__class__.PATH)

    def send_command(self, command):
        self.sio.emit('json', command)
