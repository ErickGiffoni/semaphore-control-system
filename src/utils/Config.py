import json


class Config:
    def __init__(self):
        self.configData = self.loadConfig()
        self.centralIP = self.configData["central"]["ip"]
        self.centralPort = self.configData["central"]["port"]
        self.distributedInfo = self.configData["distributed"]

    def loadConfig(self):
        with open("utils/config.json") as configFile:
            configData = json.load(configFile)
        return configData

    def whichDistributedIsAddr(self, addr):
        # addr is a pair (hostaddr: str, port: int)
        for dist in self.distributedInfo:
            if (dist["ip"], dist["port"]) == addr:
                return dist["number"]
        return None

    def getRoadTimerInfo(self, isMainRoad=True):
        return self.configData["timer"]["mainRoad" if isMainRoad else "auxRoad"]

    def getDistributedJunction(self, distributedId: int, junctionId: int):
        return self.distributedInfo[distributedId-1]["junction"][junctionId-1]

    def getDistributedLeds(self, distributedId: int, junctionId:int, trafficId: int):
        """
        distributedId: distributed server ID - either 1 or 2
        trafficId: traffic light ID - either 1 or 2
        """
        return self.getDistributedJunction(distributedId, junctionId)["leds"]\
            [trafficId-1]
