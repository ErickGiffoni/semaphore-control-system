from threading import Thread

class Road(Thread):
    def __init__(self, road, distributedServerId: int, junctionId: int, trafficLights: list):
        Thread.__init__(self)
        self.road = road
        self.distributedServerId = distributedServerId
        self.junctionId = junctionId
        self.trafficLights = trafficLights

    def run(self):
        pass
