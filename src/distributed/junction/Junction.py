from threading import Thread

from utils.Config import Config
from distributed.buzzer.Buzzer import Buzzer
from distributed.roads.AuxRoad import AuxRoad
from distributed.roads.MainRoad import MainRoad


class Junction(Thread):
   def __init__(self, junctionId: int, distributedServerId: int, config: Config):
      Thread.__init__(self)
      self.name = f"Junction number {junctionId} of distributed server {distributedServerId}"
      self.config = config
      self.mainRoad = MainRoad(distributedServerId, junctionId, self.config)
      self.auxRoad  = AuxRoad(distributedServerId, junctionId, self.config)
      self.buzzer   = Buzzer()
      
   def run(self):
      print ("Starting " + self.name)
      # do stuff
      self.mainRoad.startMonitoring()
      self.auxRoad.startMonitoring()
      # exit
      print("Exiting " + self.name)
      return