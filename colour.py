#!/usr/bin/env python3
#import stuff
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
from ev3dev2.sound import Sound
# variable setup
colorsensor = ColorSensor()
sound = Sound()
# loop
while True:
    color = colorsensor.color
    text = ColorSensor.COLORS[color]
    sound.speak(text)
    sleep(2)
