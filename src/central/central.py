import socket
import sys

from utils.Comms import Comms
from utils.Config import config

HOST = config.centralIP
PORT = config.centralPort
N_DISTRIBUTED = int(sys.argv[1])

my_con = Comms(isCentral=True, whichDistributed=0, config=config, n_distributed=N_DISTRIBUTED)
my_con.listenToDistributedServers()

while True:
    data = my_con.distributed1.recv(1024)
    print(data.decode())

my_con.closeMySocket()
