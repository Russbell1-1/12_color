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

robot.drive(20, 0)

contador=0
while 1==1:
    if color_sensor.color()==Color.BLACK:
       contador = contador + 1
       ev3.screen.clear()
       ev3.screen.print("El contador es:")
       ev3.screen.print(contador)
       

    if color_sensor.color()==Color.RED:
       robot.stop()
wait(100)





# Write your program here.

