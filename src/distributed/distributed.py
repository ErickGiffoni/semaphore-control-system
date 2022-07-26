# from utils.utils import loadConfig
# from Utils.utils import loadConfig
# from ..Utils.utils import loadConfig
import socket
from utils.utils import loadConfig


config = loadConfig()

centralIp      = config["central"]["ip"]
distributedIp1 = config["distributed"]["1"]["ip"]
distributedIp2 = config["distributed"]["2"]["ip"]

centralPort      = config["central"]["port"]
distributedPort1 = config["distributed"]["1"]["port"]
distributedPort2 = config["distributed"]["2"]["port"]

ds1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ds2 = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

ds1.bind((distributedIp1, distributedPort1))
ds2.bind((distributedIp2, distributedPort2))

ds1.connect((centralIp, centralPort))
ds2.connect((centralIp, centralPort))

print(ds1.recv(1024).decode())
print(ds2.recv(1024).decode())

ds1.close()
ds2.close()