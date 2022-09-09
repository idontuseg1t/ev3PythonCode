#!/usr/bin/env python3

from time import sleep
# ev3dev stuff
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.led import Leds

# variables
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
tank_steer = MoveSteering(OUTPUT_B, OUTPUT_C)
tank_drive.gyro = GyroSensor()
tank_drive.gyro.calibrate()
tank_drive.color = ColorSensor()


while True:
    sleep(0.01)
    if tank_drive.color.color == 1:
        tank_steer.on(steering=0, speed=10)
    else:
        tank_steer.off()
        sleep(1)
        tank_steer.on_for_rotations(0,-10,0.1)
        sleep(1)
        tank_drive.turn_left(10,20)
        sleep(1)
        if tank_drive.color.color != 1:
            tank_drive.turn_right(10,20)
            sleep(1)
            tank_steer.on_for_rotations(0,10,0.4)
            tank_drive.turn_right(10,90)
        else:
            tank_drive.turn_right(10,20)
            sleep(1)
            tank_steer.on_for_rotations(0,10,0.4)
            tank_drive.turn_left(10,90)
