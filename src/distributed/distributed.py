import socket
from sys import argv
from threading import Thread

from utils.Config import config
from distributed.TrafficLight import TrafficLight

DISTRIBUTED_ID = int(argv[1])
distributed = config.getDistributed(DISTRIBUTED_ID)
HOST = distributed["ip"]
PORT = distributed["port"]

roadLights = []
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
        timer = timer_main_road
        start_light = "green"
    else:
        timer = timer_aux_road
        start_light = "red"
    roadLights.append(TrafficLight(leds, timer, start_light, pedestrian_button))


for lights in roadLights:
    lights.start()

for lights in roadLights:
    lights.join()
