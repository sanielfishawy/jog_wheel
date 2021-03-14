from flask import Flask
from flask_socketio import SocketIO, send, emit
from werkzeug import debug

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

@socketio.on('json')
def handle_json(jsn):
    print('received json: ' + str(jsn))
    send(jsn, json=True)

@socketio.on('connect')
def test_connect():
    print('Client connected ')
    socketio.emit('my response', {'data': 'Connected'})

@socketio.on('my_message')
def handle_my_custom_event(json):
    print('received my_message: ' + str(json))

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=True, use_reloader=True, log_output=True)