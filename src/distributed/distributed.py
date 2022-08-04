from sys import argv
from distributed.Sensor import Sensor
from threading import Event


from utils.Comms import Comms
from utils.Config import config
from distributed.TrafficLight import TrafficLight
from distributed.sendSignal import sendSignal

DISTRIBUTED_ID = int(argv[1])
distributed = config.getDistributed(DISTRIBUTED_ID)
HOST = distributed["ip"]
PORT = distributed["port"]

my_con = Comms(config=config, isCentral=False, whichDistributed=DISTRIBUTED_ID)

mainRoadLight = ""
auxRoadLight = ""
timer_main_road = config.getRoadTimerInfo()
timer_aux_road = config.getRoadTimerInfo(False)
event = Event()
event2 = Event()

for trafficLight in distributed["trafficlights"]:
    leds = {
        "green": trafficLight["green"],
        "red": trafficLight["red"],
        "yellow": trafficLight["yellow"],
    }
    pedestrian_button = trafficLight["pedestrian_button"]
    if trafficLight["road"] == "main":
        mainRoadLight = TrafficLight(leds, timer_main_road, "", pedestrian_button, event, event2)
    else:
        auxRoadLight = TrafficLight(leds, timer_aux_road, "red", pedestrian_button, event, event2)

sensor = Sensor(traffic_light=mainRoadLight, pin=14)
sensor.start()

mainRoadLight.start()
auxRoadLight.start()
sendSignal.start()

mainRoadLight.join()
auxRoadLight.join()
sendSignal.join()
sensor.join()
