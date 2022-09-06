#!/usr/bin/env python3

from time import sleep
# ev3dev stuff
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.led import Leds

# variables
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
tank_steer = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_drive.gyro = GyroSensor()
tank_drive.gyro.calibrate()
tank_drive.touch = TouchSensor()

while True:
  sleep(0.01)
  motor_pair.on(steering=0, speed=10)
  if tank_drive.touch.is_pressed:
    motor_pair.off()
    tank_drive.turn_right(10, 90)
    tank_drive.on_for_seconds(20,20,5)
    tank_drive.turn_left(10,90)
    
    
