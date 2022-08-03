import socket
import sys
from utils.Config import config

HOST = config.centralIP
PORT = config.centralPort
N_DISTRIBUTED = int(sys.argv[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(N_DISTRIBUTED)
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
