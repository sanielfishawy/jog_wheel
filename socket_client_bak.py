import json
import socket
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    h = {'a':1, 'b':2}
    j = json.dumps(h)
    m = 'json ' + j
    # s.sendall(m.encode())
    s.send('hello')
    data = s.recv(1024)


print('Received', repr(data))