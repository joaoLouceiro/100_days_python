import random

import colorgram as c
import turtle as t

colors = c.extract("./image.jpg", 8)

n_dots = 10
t.colormode(255)
# t.setpos()
for row in range(0, n_dots):
    t.setpos((0.00, row * 20))
    for cell in range(0, n_dots):
        rgb = random.choice(colors).rgb
        print(rgb.r)
        t.color((rgb.r, rgb.g, rgb.b))
        t.down()
        print(t.position())
        t.dot(10)
        t.up()
        t.fd(20)

t.mainloop()
