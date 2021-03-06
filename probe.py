# -*- coding: utf-8 -*-
from random import random, randint

import simple_draw as sd

sd.resolution = (1200, 600)


def random_list(count, a, b):
    list_ = []
    for j in range(count):
        list_.append(randint(a, b))
    return list_


y = 500
snow_x = random_list(20, 90, 1060)
snow_length = random_list(20, 1, 30)
z = 0
while True:
    sd.start_drawing()
    for i in range(20):
        point = sd.get_point(snow_x[i] + z, y)
        sd.snowflake(center=point, length=snow_length[i], color=sd.background_color)
    y -= 10
    if y < 5:
        break
    z += randint(-10, 10)
    for j in range(20):
        point = sd.get_point(snow_x[j] + z, y)
        sd.snowflake(center=point, length=snow_length[j], color=sd.COLOR_WHITE)

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
#