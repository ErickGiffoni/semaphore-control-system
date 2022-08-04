from threading import Thread
from gpiozero import LED, Button
from time import perf_counter, sleep


class TrafficLight(Thread):
    def __init__(self, leds, timer, start_light, pedestrian_button, event, event2):
        Thread.__init__(self)
        self.name = "MainRoad" if pedestrian_button == 8 or pedestrian_button == 10 else "AuxRoad"
        self.green_light = LED(leds["green"])
        self.timer_green_light = timer["green"]

        self.red_light = LED(leds["red"])
        self.timer_red_light = timer["red"]
        self.timer_red_delay_light = timer["red_delay"]

        self.yellow_light = LED(leds["yellow"])
        self.timer_yellow_light = timer["yellow"]

        self.light_start_time = 0
        self.current_light = ""

        self.event = event
        self.event2 = event2
        self.pedestrian_button = Button(
            pedestrian_button, pull_up=False, bounce_time=0.35
        )
        self.pedestrian_button.when_pressed = self.button_pressed

        if start_light == "red":
            self.turn_red_light_on()
        else:
            self.turn_red_delay_light_on()

    def run(self):
        while True:
            event_is_set = self.event.wait(0)
            if event_is_set:
                wait_for_event2 = self.event2.wait()
                self.turn_green_light_on()
                self.event2.clear()
            self.change_lights()

    def button_pressed(self):
        print(f"[+] Button pressed ({self.name})")
        if self.current_light == "green":
            self.turn_yellow_light_on()
            print(f"current_light ({self.name}) => {self.current_light}")
            self.event.set()
            self.change_lights()
            self.event2.set()
            self.event.clear()

    def change_lights(self):
        print(f"current_light ({self.name}) => {self.current_light}")
        if self.current_light == "red_delay":
            self.wait_and_then_change(
                self.timer_red_delay_light, self.turn_green_light_on
            )
        elif self.current_light == "green":
            self.wait_and_then_change(self.timer_green_light, self.turn_yellow_light_on)
        elif self.current_light == "yellow":
            self.wait_and_then_change(self.timer_yellow_light, self.turn_red_light_on)
        elif self.current_light == "red":
            self.wait_and_then_change(
                self.timer_red_light, self.turn_red_delay_light_on
            )

    def turn_red_light_on(self):
        self.__turn_light_on("red", self.red_light, self.yellow_light, self.green_light)

    def turn_red_delay_light_on(self):
        self.__turn_light_on(
            "red_delay", self.red_light, self.yellow_light, self.green_light
        )

    def turn_green_light_on(self):
        self.__turn_light_on(
            "green", self.green_light, self.yellow_light, self.red_light
        )

    def turn_yellow_light_on(self):
        self.__turn_light_on(
            "yellow", self.yellow_light, self.red_light, self.green_light
        )

    def __turn_light_on(self, light_name, light_on, light_off1, light_off2):
        self.light_start_time = perf_counter()
        self.current_light = light_name
        light_off1.off()
        light_off2.off()
        light_on.on()

    def wait_and_then_change(self, min_light_time, turn_light_on):
        while perf_counter() < self.light_start_time + min_light_time:
            pass
        turn_light_on()
