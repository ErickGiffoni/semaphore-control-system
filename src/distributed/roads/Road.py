class Road:
    def __init__(self, road, distributedServerId: int, junctionId: int, trafficLights: list):
        self.road = road
        self.distributedServerId = distributedServerId
        self.junctionId = junctionId
        self.trafficLights = trafficLights

    def startMonitoring(self):
        pass
