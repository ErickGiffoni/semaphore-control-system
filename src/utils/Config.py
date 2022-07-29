import json


class Config:
    def __init__(self):
        configData = self.loadConfig()
        self.centralIP = configData["central"]["ip"]
        self.centralPort = configData["central"]["port"]
        self.distributedInfo = configData["distributed"]

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
