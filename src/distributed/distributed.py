import socket
from sys import argv
from threading import Thread

from utils.Config import config
from distributed.TrafficLight import TrafficLight

DISTRIBUTED_ID = int(argv[1])
distributed = config.getDistributed(DISTRIBUTED_ID)
HOST = distributed["ip"]
PORT = distributed["port"]

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b'Hello, world')
#    data = s.recv(1024)
#
# print('Received', data)

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
    timer = timer_main_road if trafficLight["road"] == "main" else timer_aux_road
    roadLights.append(TrafficLight(leds, timer, pedestrian_button))


for lights in roadLights:
    lights.start()

for lights in roadLights:
    lights.join()
