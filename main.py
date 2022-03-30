#!/usr/bin/env python3

import os
from ev3dev2.motor import MoveSteering ,OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.button import Button
import Rclass

os.system('setfont Vietnamese-Fixed13')

cs_l = ColorSensor(INPUT_1)
cs_r = ColorSensor(INPUT_2)
tank = MoveSteering(OUTPUT_A, OUTPUT_B)
btn = Button()

Pctr = Rclass.Pctr(tank, cs_l, cs_r)

print('start')
while True:
    Pctr.run(-20, 0.20)