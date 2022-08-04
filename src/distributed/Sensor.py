import RPi.GPIO as GPIO
from threading import Thread

from distributed.TrafficLight import TrafficLight


class Sensor(Thread):
   def __init__(self, pin, traffic_light: TrafficLight) -> None:
      Thread.__init__(self)
      self.pin = pin
      self.traffic_light = traffic_light
      self.qtt_cars_crossed_red = 0
      self.qtt_cars_total = 0

      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

   def run(self):
      while True:
         input = GPIO.input(self.pin)
         if input == True:
            print("passou carro ai mano")
            if self.traffic_light.current_light == "red":
               self.qtt_cars_crossed_red += 1
            
            self.qtt_cars_total += 1
