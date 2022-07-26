import socket

import utils.utils as utils

class Comms():
   def __init__(self, isCentral=False) -> None:
      self.isCentral = False
      self.mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

      if isCentral:
         self.isCentral = True
         self.distributed1 = socket.socket
         self.distributed2 = socket.socket

         centralIp, centralPort = utils.getCentralInfo()
         print(centralIp, centralPort)
         try:
            self.mySocket.bind((centralIp, centralPort))
         except:
            print("Error: Comms failed to bind central socket")

      else:
         self.central = 0
      self.message = ""

   def listenToDistributedServers(self):
      if self.isCentral:
         self.mySocket.listen(2)
         distributed1Connected = False
         distributed2Connected = False
         while True:
            conn, addr = self.mySocket.accept()
            distributed = utils.whichDistributedIsAddr(addr)

            if distributed == None:
               conn.send("You are not allowed".encode())
               conn.close()

            elif distributed == 1:
               self.distributed1 = conn
               print(f"[.] {addr} connected")
               distributed1Connected = True

            elif distributed == 2:
               self.distributed2 = conn
               print(f"[.] {addr} connected")
               distributed2Connected = True

            if distributed1Connected and distributed2Connected:
               print("[.] Both distributed servers are connected")
               break
   
      else:
         print("Error: listenToDistributedServers - only the central server\n\
            can listen to connections"
         )
      
      return