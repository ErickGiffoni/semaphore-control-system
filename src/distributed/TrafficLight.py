from threading import Thread
from gpiozero import LED, Button
from time import perf_counter

class TrafficLight(Thread):
    def __init__(self, leds, timer, pedestrian_button):
        Thread.__init__(self)
        self.green_light = LED(leds["green"])
        self.timer_green_light = timer["green"]

        self.red_light = LED(leds["red"])
        self.timer_red_light = timer["red"]

        self.yellow_light = LED(leds["yellow"])
        self.timer_yellow_light = timer["yellow"]

        self.light_start_time = 0
        self.current_light = ""
        self.turn_red_light_on()

        self.pedestrian_button = Button(pedestrian_button, pull_up=False, bounce_time=0.35)
        # self.pedestrian_button.when_pressed = self.turn_red_traffic_light_on
        self.pedestrian_button.when_pressed = self.button_pressed

    def run(self):
        while True:
            print(f"current_light => {self.current_light}")
            self.change_lights()

    def button_pressed(self):
        print("[+] Button pressed")
        if self.current_light == "yellow":
            self.wait_and_then_change(self.timer_yellow_light, self.turn_red_light_on)
        elif self.current_light == "green":
            self.wait_and_then_change(self.timer_green_light, self.turn_yellow_light_on)
            self.wait_and_then_change(self.timer_green_light, self.turn_red_light_on)

    def change_lights(self):
        if self.current_light == "red":
            self.wait_and_then_change(self.timer_red_light, self.turn_green_light_on)
        if self.current_light == "yellow":
            self.wait_and_then_change(self.timer_yellow_light, self.turn_red_light_on)
        if self.current_light == "green":
            self.wait_and_then_change(self.timer_green_light, self.turn_yellow_light_on)

    def turn_red_traffic_light_on(self):
        while self.current_light != "red":
            self.change_lights()

    def turn_red_light_on(self):
        self.__turn_light_on("red", self.red_light, self.yellow_light, self.green_light)

    def turn_green_light_on(self):
        self.__turn_light_on("green", self.green_light, self.yellow_light, self.red_light)

    def turn_yellow_light_on(self):
        self.__turn_light_on("yellow", self.yellow_light, self.red_light, self.green_light)

    def __turn_light_on(self, light_name, light_on, light_off1, light_off2):
        light_off1.off()
        light_off2.off()
        light_on.on()
        self.light_start_time = perf_counter()
        self.current_light = light_name

    def wait_and_then_change(self, min_light_time, turn_light_on):
        while perf_counter() < self.light_start_time + min_light_time:
            pass
        turn_light_on()
