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
        if (self.distributed["1"]["ip"], self.distributed["1"]["port"]) == addr:
            return 1
        
        elif (self.distributed["2"]["ip"], self.distributed["2"]["port"]) == addr:
            return 2

        elif (self.distributed["3"]["ip"], self.distributed["3"]["port"]) == addr:
            return 3

        elif (self.distributed["4"]["ip"], self.distributed["4"]["port"]) == addr:
            return 4

        return None

    def getRoadTimerInfo(self, isMainRoad=True):
        return self.timer["mainRoad" if isMainRoad else "auxRoad"]

    def getDistributed(self, distributed_id):
        return self.distributed[str(distributed_id)]

    def __loadConfig(self):
        with open("utils/config.json") as configFile:
            configData = json.load(configFile)
        return configData


config = Config()
