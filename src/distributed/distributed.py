from sys import argv
from distributed.Sensor import Sensor


from utils.Comms import Comms
from utils.Config import config
from distributed.TrafficLight import TrafficLight

DISTRIBUTED_ID = int(argv[1])
distributed = config.getDistributed(DISTRIBUTED_ID)
HOST = distributed["ip"]
PORT = distributed["port"]

my_con = Comms(config=config, isCentral=False, whichDistributed=DISTRIBUTED_ID)

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

sensor = Sensor(mainRoadLight, pin=14)
sensor.start()

mainRoadLight.start()
auxRoadLight.start()

mainRoadLight.join()
auxRoadLight.join()
sensor.join()
