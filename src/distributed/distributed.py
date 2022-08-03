import socket
from sys import argv
from threading import Thread

from utils.Config import config
from distributed.TrafficLight import TrafficLight

DISTRIBUTED_ID = int(argv[1])
distributed = config.getDistributed(DISTRIBUTED_ID)
HOST = distributed["ip"]
PORT = distributed["port"]

mainRoadLight = ""
auxRoadLight = ""
timer_main_road = config.getRoadTimerInfo()
timer_aux_road = config.getRoadTimerInfo(False)

for trafficLight in distributed["trafficlights"]:
    leds = {
        "green": trafficLight["green"],
        "red": trafficLight["red"],
        "yellow": trafficLight["yellow"],
    }
    pedestrian_button = trafficLight["pedestrian_button"]
    if trafficLight["road"] == "main":
        mainRoadLight = TrafficLight(leds, timer_main_road, "", pedestrian_button)
    else:
        auxRoadLight = TrafficLight(leds, timer_aux_road, "red", pedestrian_button)

mainRoadLight.start()
auxRoadLight.start()

mainRoadLight.join()
auxRoadLight.join()
