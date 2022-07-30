from utils.Config import Config
from distributed.roads.Road import Road
from distributed.traffic_light.TrafficLight import TrafficLight


class AuxRoad(Road):
   def __init__(self, distributedServerId: int, junctionId: int, config: Config):
      Road.__init__(self, distributedServerId, junctionId, config)
      timer = self.config.getRoadTimerInfo(isMainRoad=False)

      self.trafficLight1 = TrafficLight(
         self.config.getDistributedLeds(distributedServerId, junctionId, 1),
         timer
      )
      self.trafficLight2 = TrafficLight(
         self.config.getDistributedLeds(distributedServerId, junctionId, 2),
         timer
      )

   def startMonitoring(self):
      print("[.] Aux Road initiating...")