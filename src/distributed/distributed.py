from sys import argv
from distributed.Sensor import Sensor
from threading import Event
import signal

from utils.Comms import Comms
from utils.Config import config
from distributed.TrafficLight import TrafficLight
from distributed.sendSignal import sendSignal

def send_messages_to_central_server(signum, frame):
    print("sending message to central server!")
    message = f"Hello from {DISTRIBUTED_ID}"
    my_con.mySocket.send(message.encode())

signal.signal(signal.SIGUSR1, send_messages_to_central_server)

DISTRIBUTED_ID = int(argv[1])
distributed = config.getDistributed(DISTRIBUTED_ID)
HOST = distributed["ip"]
PORT = distributed["port"]

my_con = Comms(config=config, isCentral=False, whichDistributed=DISTRIBUTED_ID)

mainRoadLight = ""
mainRoadSensor = ""
auxRoadLight = ""
auxRoadSensor = ""
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
        mainRoadSensor = Sensor(traffic_light=mainRoadLight, pin=trafficLight["sensor"])
    else:
        auxRoadLight = TrafficLight(leds, timer_aux_road, "red", pedestrian_button, event, event2)
        auxRoadSensor = Sensor(traffic_light=mainRoadLight, pin=trafficLight["sensor"])

mainRoadLight.start()
mainRoadSensor.start()
auxRoadLight.start()
auxRoadSensor.start()
sendSignal.start()

mainRoadLight.join()
mainRoadSensor.join()
auxRoadLight.join()
auxRoadSensor.join()
sendSignal.join()
