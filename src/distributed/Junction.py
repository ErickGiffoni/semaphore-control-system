import json
from threading import Thread
from distributed.buzzer.Buzzer import Buzzer
from distributed.Road import Road


class Junction(Thread):
    def __init__(self, distributedServerId: int, junctionConfig: json):
        Thread.__init__(self)
        self.junctionId = junctionConfig["id"]
        self.name = (
            f"Junction number {self.junctionId} of distributed server {distributedServerId}"
        )
        mainRoadLights = []
        auxRoadLights = []
        for trafficLight in junctionConfig["trafficlights"]:
            if trafficLight["road"] == "main":
                mainRoadLights.append(trafficLight)
            else:
                auxRoadLights.append(trafficLight)
        self.mainRoad = Road(
            "main",
            distributedServerId,
            self.junctionId,
            mainRoadLights
        )
        self.auxRoad = Road(
            "aux",
            distributedServerId,
            self.junctionId,
            auxRoadLights
        )
        self.buzzer = Buzzer()

    def run(self):
        print("Starting " + self.name)
        self.mainRoad.start()
        self.auxRoad.start()
        self.mainRoad.join()
        self.auxRoad.join()
        print("Exiting " + self.name)
        return
