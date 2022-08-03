import socket
import sys
from utils.Config import config
from distributed.TrafficLight import TrafficLight

DISTRIBUTED_ID = int(sys.argv[1])
distributed = config.getDistributed(DISTRIBUTED_ID)
HOST = distributed["ip"]
PORT = distributed["port"]

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b'Hello, world')
#    data = s.recv(1024)
#
# print('Received', data)

mainRoadLights = []
timer_main_road = config.getRoadTimerInfo()

auxRoadLights = []
timer_aux_road = config.getRoadTimerInfo(False)

for trafficLight in distributed["trafficlights"]:
    leds = {
        trafficLight["green"],
        trafficLight["red"],
        trafficLight["yellow"]
    }
    pedestrian_button = trafficLight["pedestrian_button"]
    if trafficLight["road"] == "main":
        mainRoadLights.append(TrafficLight(leds, timer_main_road, pedestrian_button))
    else:
        auxRoadLights.append(TrafficLight(leds, timer_aux_road, pedestrian_button))

print(mainRoadLights)
print(auxRoadLights)
