import socketio

sio = socketio.Client()

sio.connect('http://localhost:5000')
sio.emit('my_message', {'foo': 'bar'})
sio.emit('my_message', {'bar': 'baz'})
sio.emit('json', {'for': 'json'})
sio.disconnect()
pass