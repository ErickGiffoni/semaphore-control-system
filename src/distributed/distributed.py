from threading import Thread
from time import sleep

from utils.Comms import Comms
from .junction.Junction import Junction


class Distributed(Thread):
   def __init__(self, distributedId: int) -> None:
      """
      distributedId is either 1 or 2
      """
      Thread.__init__(self)
      self.name = f"Distributed Server {distributedId}"
      self.comms = Comms(isCentral=False, whichDistributed=distributedId)
      self.junction1 = Junction(
         junctionId=1, distributedServerId=distributedId, config=self.comms.config
      )
      self.junction2 = Junction(
         junctionId=2, distributedServerId=distributedId, config=self.comms.config
      )


   def run(self):
      print ("Starting " + self.name)
      # start junctions
      self.junction1.start()
      self.junction2.start()

      sleep(1)
      print ("Exiting " + self.name)
      # join junctions
      self.junction1.join()
      self.junction2.join()

      # close socket
      self.comms.closeMySocket()
      return

d  = Distributed(1)
d2 = Distributed(2)

d.start()
d2.start()

d.join()
d2.join()
