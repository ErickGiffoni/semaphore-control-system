from time import sleep
from utils.Comms import Comms

class Central():
   def __init__(self) -> None:
      self.comms = Comms(isCentral=True, whichDistributed=0)
      self.comms.listenToDistributedServers()
      sleep(1)
      self.comms.closeMySocket()



c = Central()


# config = loadConfig()

# centralIp      = config["central"]["ip"]
# distributedIp1 = config["distributed"]["1"]["ip"]
# distributedIp2 = config["distributed"]["2"]["ip"]

# centralPort      = config["central"]["port"]
# distributedPort1 = config["distributed"]["1"]["port"]
# distributedPort2 = config["distributed"]["2"]["port"]

# ds1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# # ds2 = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# ds1.bind((centralIp, centralPort))
# # ds2.bind((distributedIp2, centralPort))

# ds1.listen(2)

# while True:
#    conn, addr = ds1.accept()
#    print(f"[x] {addr} connected")
#    conn.send("It worked\n".encode())
#    conn.close()