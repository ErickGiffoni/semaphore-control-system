from threading import Thread
from gpiozero import Button
 
class PedestrianButton(Thread):
    def __init__(self, button, traffic_light):
        self.button = Button(button)
        self.button.when_pressed = self.turn_red_traffic_light_on
        self.traffic_light = traffic_light

    def turn_red_traffic_light_on(self):
        # we need to stop the road normal flow here before calling change_lights
        while self.traffic_light.current_light != "red":
            self.traffic_light.change_lights()
