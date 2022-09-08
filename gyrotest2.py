#!/usr/bin/env python3

from time import sleep
# ev3dev stuff
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.led import Leds

# variables
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
tank_steer = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_drive.gyro = GyroSensor()
tank_drive.gyro.calibrate()
tank_drive.sonic = UltrasonicSensor()
# main loop
while True:
  sleep(0.01)
  tank_steer.on(steering=0, speed=10)
  if tank_drive.sonic.distance_centimeters < 6:
    tank_steer.off()
    tank_drive.turn_right(10, 90)
    tank_drive.on_for_seconds(20,20,5)
    tank_drive.turn_left(10,90)
    
    
