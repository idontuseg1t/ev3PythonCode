#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor

motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
touch_sensor = TouchSensor()

motor_pair.on(steering=0, speed=20)
touch_sensor.wait_for_pressed()
motor_pair.off()
motor_pair.on_for_seconds(steering=0, speed=-20, seconds=4)
