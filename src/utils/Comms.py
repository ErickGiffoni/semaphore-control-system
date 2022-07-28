import socket

import utils.utils as utils

class Comms():
   def __init__(self, isCentral: bool, whichDistributed: int) -> None:
      self.isCentral = isCentral
      self.mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
      self.message = ""
      centralIp, centralPort = utils.getCentralInfo()

      if isCentral:
         self.distributed1 = socket.socket
         self.distributed2 = socket.socket

         self.mySocket.bind((centralIp, centralPort))
         
      # It is a distributed server
      else:
         if 1 > whichDistributed or 2 < whichDistributed:
            raise Exception(f"CommsException: whichDistributed out of range: {whichDistributed}")

         dist1Info, dist2Info = utils.getDistributedInfo()
         bindAddrs = (dist1Info[0], dist1Info[1]) if whichDistributed == 1 else \
                     (dist2Info[0], dist2Info[1])

         self.mySocket.bind(bindAddrs)
         self.mySocket.connect((centralIp, centralPort))
         print(self.mySocket.recv(1024).decode())

   def closeMySocket(self):
      self.mySocket.close()
      return

   def listenToDistributedServers(self):
      if self.isCentral:
         self.mySocket.listen(2)
         distributed1Connected = False
         distributed2Connected = False
         while True:
            print("[...] Central server waiting connections from distributed servers")
            conn, addr = self.mySocket.accept()
            distributed = utils.whichDistributedIsAddr(addr)

            if distributed == None:
               conn.send("You are not allowed".encode())
               conn.close()

            elif distributed == 1:
               self.distributed1 = conn
               print(f"[.] {addr} connected: 1")
               self.distributed1.send("[.] CONNECTED: 1".encode())
               distributed1Connected = True

            elif distributed == 2:
               self.distributed2 = conn
               print(f"[.] {addr} connected: 2")
               self.distributed2.send("[.] CONNECTED: 2".encode())
               distributed2Connected = True

            if distributed1Connected and distributed2Connected:
               print("[.] Both distributed servers are connected")
               break
   
      else:
         print("Comms Alert: listenToDistributedServers - only the central server\n\
            can listen to connections"
         )
      
      return