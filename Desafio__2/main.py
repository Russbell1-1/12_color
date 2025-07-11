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



Mi.run(200)
Md.run(200)

while 1==1:
    if (color_sensor.color()==Color.RED):
        Mi.stop()
        Md.stop()


# Write your program here.


# Write your program here.

