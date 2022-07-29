from threading import Thread
from gpiozero import LED


class TrafficLight(Thread):
    def __init__(self, green_led, red_led, yellow_led):
        Thread.__init__(self)
        self.green_light = LED(green_led)
        self.red_light = LED(red_led)
        self.yellow_light = LED(yellow_led)

    def turn_red_light_on():
        self.__turn_light_on(self.red_light, self.yellow_light, self.green_light)

    def turn_green_light_on():
        self.__turn_light_on(self.green_light, self.yellow_light, self.red_light)

    def turn_yellow_light_on():
        self.__turn_light_on(self.yellow_light, self.red_light, self.green_light)

    def __turn_light_on(light_on, light_off1, light_off2):
        self.light_on.on()
        self.light_off1.off()
        self.light_off2.off()
