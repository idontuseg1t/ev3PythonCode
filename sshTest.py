#!/usr/bin/env python3
# so that script can be run from Brickman
# most is from https://github.com/peprolinbot/EV3D4-ssh_control/blob/master/conbot.py
# but modifications such as speed control have been made
import subprocess
import termios, tty, sys
from ev3dev.ev3 import *

# attach large motors to ports B and C, medium motor to port A
motor_left = LargeMotor('outC')
motor_right = LargeMotor('outB')
speed = 500
# motor_a = MediumMotor('outA')

#==============================================
print("\n=========READY============\n\n\n\n============LOG============\n")
#==============================================
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return ch

#==============================================



#==============================================

def forward():
   motor_left.run_forever(speed_sp=speed)
   motor_right.run_forever(speed_sp=speed)

#==============================================

def back():
   motor_left.run_forever(speed_sp=-(speed))
   motor_right.run_forever(speed_sp=-(speed))

#==============================================

def left():
   motor_left.run_forever(speed_sp=-250)
   motor_right.run_forever(speed_sp=250)

#==============================================

def right():
   motor_left.run_forever(speed_sp=250)
   motor_right.run_forever(speed_sp=-250)

#==============================================

def stop():
   motor_left.run_forever(speed_sp=0)
   motor_right.run_forever(speed_sp=0)

#==============================================

while True:
   k = getch()
   print(k)

   if k == 'w':
      forward()
   if k == 's':
      back()
   if k == 'a':
      right()
   if k == 'd':
      left()
   if k == ' ':
      stop()
   if k == 'q':
      exit()
   if k == 'e':
       speed += 50
       print(speed)
   if k == 'r':
       speed -= 50
       print(speed)
