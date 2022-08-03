import socket
import sys
from utils.Config import config

HOST = '192.168.0.8'
PORT = 50007
DISTRIBUTED_ID = int(sys.argv[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', data)
