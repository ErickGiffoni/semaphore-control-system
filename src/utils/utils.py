import json


def loadConfig():
    with open("utils/config.json") as configFile:
        configData = json.load(configFile)
    return configData


def getCentralInfo():
    central = loadConfig()["central"]
    return central["ip"], central["port"]


def getDistributedInfo():
    return loadConfig()["distributed"]


def whichDistributedIsAddr(addr):
    # addr is a pair (hostaddr: str, port: int)
    for dist in getDistributedInfo():
        if (dist["ip"], dist["port"]) == addr:
            return dist["number"]
    return None
