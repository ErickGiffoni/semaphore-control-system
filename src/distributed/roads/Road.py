from distributed.traffic_light.TrafficLight import TrafficLight
from utils.Config import Config


class Road:
   def __init__(self, distributedServerId: int, junctionId: int, config: Config):
      self.distributedServerId = distributedServerId
      self.junctionId          = junctionId
      self.config              = config

      self.trafficLight1: TrafficLight
      self.trafficLight2: TrafficLight

   def startMonitoring(self):
      """Override this method in a subclass"""
      pass