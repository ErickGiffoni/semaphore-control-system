import json


def loadConfig():
   with open("utils/config.json") as configFile:
      configData = json.load(configFile)
   return configData