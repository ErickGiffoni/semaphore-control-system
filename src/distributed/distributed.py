from threading import Thread
from time import sleep

from utils.Comms import Comms

class Distributed(Thread):
   def __init__(self, distributedId: int) -> None:
      """
      distributedId is either 1 or 2
      """
      Thread.__init__(self)
      self.name = f"Distributed Server {distributedId}"
      self.comms = Comms(isCentral=False, whichDistributed=distributedId)
      self.comms.closeMySocket()

   def run(self):
      print ("Starting " + self.name)
      sleep(1)
      print ("Exiting " + self.name)
      return

d  = Distributed(1)
d2 = Distributed(2)

d.start()
d2.start()

d.join()
d2.join()
