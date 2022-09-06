#!/usr/bin/env python3

from time import sleep
# ev3dev stuff
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.led import Leds


tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
tank_drive.gyro = GyroSensor()
tank_drive.gyro.calibrate()

tank_drive.on_for_seconds(60,60,5)

tank_drive.turn_degrees(
    speed=SpeedPercent(5),
    target_angle=45
)
