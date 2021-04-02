import time
import logging
import socketio


class Commands:
    SAVE_POSITION = 'save_position'
    CHANGE_POSITION = 'change_position'
    UPDATE_STATE = 'update_state'
    FIND_STOPS = 'find_stops'
    CLEAR_ERRORS = 'clear_errors'
    SAVE_REVOLUTIONS_PER_INCH = 'save_revolutions_per_inch'
    SAVE_ZERO_POSITION = 'save_zero_position'


class CommandTransmitter:

    _instance = None
    SERVER_PATH = 'http://192.168.1.159:80'

    def __init__(self):
        self.setup_logging()

        if self.__class__._instance:
            raise "Command Transmitter is a singleton. Use get_instance() to get the instance."

        self.sio = socketio.Client()
        self.connected = False
        self.connect_to_server()

        self.sio.on('connect', self.connect_handler)
        self.sio.on('disconnect', self.disconnect_handler)
        self.sio.on(Commands.UPDATE_STATE, self.update_state_handler)

        self.__class__._instance = self

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls()
        return cls._instance

    def setup_logging(self):
        self.logger = logging.getLogger()
        self.logger.name = self.__class__.__name__
        self.logger.info('test')
    
    def connect_to_server(self):
        self.logger.info('in connect to server')
        while not self.connected:
            try:
                self.sio.connect(self.__class__.SERVER_PATH)
                self.logger.info('Connected')
                self.connected = True
            except socketio.exceptions.ConnectionError as err:
                self.logger.error(f'Connecting to {self.__class__.SERVER_PATH} {str(err)}')
                time.sleep(1)
            except:
                raise
        
    def change_position(self, change_inches):
        self.sio.emit(Commands.CHANGE_POSITION, change_inches)
    
    def connect_handler(self):
        self.logger.info("Connect")
    
    def disconnect_handler(self):
        self.logger.info("Disconnect")
    
    def update_state_handler(self, msg):
        self.logger.debug(f"update_state {msg}")