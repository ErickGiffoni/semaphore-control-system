import json


def loadConfig():
   with open("utils/config.json") as configFile:
      configData = json.load(configFile)
   return configData

def getCentralInfo():
   config = loadConfig()
   centralIp         = config["central"]["ip"]
   centralPort       = config["central"]["port"]
   return centralIp, centralPort

def getDistributedInfo():
   config = loadConfig()
   distributedIp1    = config["distributed"]["1"]["ip"]
   distributedPort1  = config["distributed"]["1"]["port"]
   distributedIp2    = config["distributed"]["2"]["ip"]
   distributedPort2  = config["distributed"]["2"]["port"]

   return (distributedIp1, distributedPort1), (distributedIp2, distributedPort2)

def whichDistributedIsAddr(addr):
   # addr is a pair (hostaddr: str, port: int)
   dst1, dst2 = getDistributedInfo()
   if dst1[0] == addr[0] and dst1[1] == addr[1]:
      return 1

   elif dst2[0] == addr[0] and dst2[1] == addr[1]:
      return 2

   else:
      return None
