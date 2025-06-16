#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
color_sensor = ColorSensor(Port.S3)

# Create your objects here.
ev3 = EV3Brick()


while 1==1:
  color = color_sensor.color()
  ev3.screen.clear()
  ev3.screen.print("El color es")
  ev3.screen.print(color)
  wait(3000)

# Write your program here.
