from tkinter import *
from math import pi, cos, sin
import time

root = Tk()
reverse, speed = True, 0.2


def inc_speed():
    global speed
    speed = speed * 0.75


def dec_speed():
    global speed
    speed = speed * 1.5


def rev():
    global reverse
    if reverse:
        reverse = False
    else:
        reverse = True


button1 = Button(text='Увеличить скорость', command=inc_speed)
button2 = Button(text='Уменьшить скорость', command=dec_speed)
button3 = Button(text='В обратную сторону', command=rev)
button1.pack()
button2.pack()
button3.pack()


def motion():
    n = 500
    x = 295
    dtheta = (2 * pi) / n
    r = 200
    xc = x - r
    yc = r
    theta = 0
    for i in range(10):
        for a in range(n):
            if reverse:
                theta -= dtheta
            else:
                theta += dtheta
            x = 295 + (r * cos(theta))
            y = 295 + (r * sin(theta))
            point = c.create_oval(x, y, x + 10, y + 10, fill='red', tag='point')
            root.update()
            time.sleep(speed)
            c.delete('point')
            root.update()


c = Canvas(root, width=600, height=600, bg="white")
c.pack()
trajectory = c.create_oval(100, 100, 500, 500, outline='green')
motion()
root.mainloop()
