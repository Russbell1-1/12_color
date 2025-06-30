#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
Mi = Motor(Port.B)
Md = Motor(Port.D)
color_sensor = ColorSensor(Port.S1)
robot = DriveBase(Mi,Md, wheel_diameter=55.5, axle_track=104)
Mi.reset_angle(0)



while color_sensor.reflection()!=90:
    reflect = color_sensor.reflection()
    if reflect<=30:
       robot.drive(40,50)
       wait(10)
    elif reflect>=30:
       robot.drive(40,-50)
       wait(10)
    
    ev3.screen.clear()
    ev3.screen.print(reflect)
    wait(200)
