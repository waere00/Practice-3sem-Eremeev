import random
from tkinter import *
import time

root = Tk()
c = Canvas(root, width=600, height=600, background='black')
c.pack()
raindrops = []
raindrops_x = []
raindrops_y = []
raindrops_height = []
raindrops_speed = []
raindrops_color = []
n = 175
for i in range(n):
    raindrops.append('')
    raindrops_y.append(random.randint(-100, 600))
    raindrops_x.append(random.randint(0, 600))
    raindrops_height.append(random.randint(1, 50))
    if raindrops_height[i] < 10:
        raindrops_speed.append(random.randint(3, 5))
        raindrops_color.append('cyan')
    if raindrops_height[i] > 25:
        raindrops_speed.append(random.randint(15, 25))
        raindrops_color.append('CornflowerBlue')
    else:
        raindrops_speed.append(random.randint(9, 12))
        raindrops_color.append('aqua')
for frame in range(1000):
    for i in range(n):
        raindrops[i] = c.create_rectangle(raindrops_x[i], raindrops_y[i], raindrops_x[i] + 4,
                                          raindrops_y[i] + raindrops_height[i], fill=raindrops_color[i])
        raindrops_y[i] += raindrops_speed[i]
        if raindrops_y[i] > 600:
            raindrops_y[i] = -raindrops_height[i]
    c.update()
    time.sleep(0.03)
    for b in range(n):
        c.delete(raindrops[b])
