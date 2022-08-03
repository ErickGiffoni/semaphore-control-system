import json


class Config:
    def __init__(self):
        configData = self.__loadConfig()
        self.centralIP = configData["central"]["ip"]
        self.centralPort = configData["central"]["port"]
        self.distributed = configData["distributed"]
        self.timer = configData["timer"]

    def getRoadTimerInfo(self, isMainRoad=True):
        return self.timer["mainRoad" if isMainRoad else "auxRoad"]

    def getDistributed(self, distributed_id):
        return self.distributed[str(distributed_id)]

    def __loadConfig(self):
        with open("utils/config.json") as configFile:
            configData = json.load(configFile)
        return configData


config = Config()
