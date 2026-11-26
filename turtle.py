import sys, os
_here = os.path.dirname(os.path.abspath(__file__))
sys.path = [p for p in sys.path if os.path.abspath(p or os.getcwd()) != _here]
sys.modules.pop('turtle', None)

import turtle as tur
import colorsys as cs

tur.setup(800, 800)
tur.bgcolor('black')
tur.title('Rainbow Flower')
tur.hideturtle()
tur.speed(0)
tur.tracer(3)
tur.width(1.5)

PETALS = 18
LINES = 16
CENTER = 45
BIG = 260
TWIST = 18

def leaf(r):
    tur.circle(r, 60)
    tur.left(120)
    tur.circle(r, 60)
    tur.left(120)

for k in range(PETALS):
    angle = k * 360 / PETALS

    tur.penup()
    tur.goto(0, 0)
    tur.setheading(angle)
    tur.forward(CENTER)
    tur.setheading(angle - 30 + TWIST)
    tur.pendown()

    hue = k / PETALS
    for j in range(LINES):
        r = BIG - j * (BIG - 30) / LINES
        sat = j / (LINES - 1)
        tur.pencolor(cs.hsv_to_rgb(hue, sat, 1))
        leaf(r)

tur.penup()
tur.goto(0, -CENTER + 8)
tur.setheading(0)
tur.pendown()
tur.pencolor('white')
tur.circle(CENTER - 8)

tur.update()
tur.done()