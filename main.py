#!/usr/bin/env python3

import os
from ev3dev2.motor import MoveSteering ,OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.button import Button

os.system('setfont Vietnamese-Fixed13')

cs_l = ColorSensor(INPUT_1)
cs_r = ColorSensor(INPUT_2)
tank = MoveSteering(OUTPUT_A, OUTPUT_B)

btn = Button()

p = 1.00
speed = -20

print('start')
while True:
    if btn.top:
        p += 0.05
        print('p:', p)
        btn.wait_for_released('top')

    elif btn.bottom:
        p -= 0.05
        print('p:', p)
        btn.wait_for_released('bottom')
    
    reflected_light_l = cs_l.reflected_light_intensity
    reflected_light_r = cs_r.reflected_light_intensity

    tank_steering = (reflected_light_l - reflected_light_r) * p

    tank.on(tank_steering, speed)