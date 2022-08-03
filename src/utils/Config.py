import json


class Config:
    def __init__(self):
        configData = self.__loadConfig()
        self.centralIP = configData["central"]["ip"]
        self.centralPort = configData["central"]["port"]
        self.distributed = configData["distributed"]
        self.timer = configData["timer"]

    def whichDistributedIsAddr(self, addr):
        """
        addr is a pair (hostaddr: str, port: int)
        """
        for dist in self.distributed:
            if (dist["ip"], dist["port"]) == addr:
                return dist["id"]
        return None

    def getRoadTimerInfo(self, isMainRoad=True):
        return self.timer["mainRoad" if isMainRoad else "auxRoad"]

    def getJunction(self, distId: int, junctionId: int):
        """
        distId: distributed server ID - either 1 or 2
        """
        return self.distributed[distId - 1]["junction"][junctionId - 1]

    def __loadConfig(self):
        with open("utils/config.json") as configFile:
            configData = json.load(configFile)
        return configData

config = Config()
