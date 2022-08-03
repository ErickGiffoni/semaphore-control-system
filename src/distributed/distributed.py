import socket
import sys
from utils.Config import config

DISTRIBUTED_ID = int(sys.argv[1])
distributed = config.getDistributed(DISTRIBUTED_ID)
HOST = distributed["ip"]
PORT = distributed["port"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', data)
