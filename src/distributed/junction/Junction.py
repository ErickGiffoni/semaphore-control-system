from threading import Thread


class Junction(Thread):
   def __init__(self, junctionId: int, distributedServerId):
      Thread.__init__(self)
      self.name = f"Junction number {junctionId} of distributed server {distributedServerId}"
      
   def run(self):
      print ("Starting " + self.name)
      # do stuff
      # exit
      print("Exiting " + self.name)
      return