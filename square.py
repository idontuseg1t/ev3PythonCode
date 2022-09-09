#!/usr/bin/env python3

from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import GyroSensor


motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor()
gyro.mode = GyroSensor.MODE_GYRO_ANG

for i in range(4):


    motor_pair.on_for_seconds(steering=0, speed=50, seconds=3)


    motor_pair.on(steering=-100, speed=5)


    gyro.wait_until_angle_changed_by(90)

    motor_pair.off()
