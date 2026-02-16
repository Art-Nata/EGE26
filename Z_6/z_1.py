from turtle import *

maxx = Turtle()

tracer(0)
maxx.pensize(3)
k = 40

for i in range(42):
    rt(60)
    fd(7 * k)
    rt(60)

for i in range(-20, 20):
    for j in range(-20, 20):
        maxx.pu()
        maxx.goto(i * k, j * k)
        maxx.pd()
        maxx.dot(3)


done()