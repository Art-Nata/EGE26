from turtle import *
print(35 * 24 + 36 * 20 - 7 * 31)
maxx = Turtle()
tracer(0)
maxx.pensize(2)

k = 20

maxx.pd()
for i in range(5):
    maxx.fd(35 * k)
    maxx.rt(90)
    maxx.fd(24 * k)
    maxx.rt(90)
maxx.pu()
maxx.rt(90)
maxx.fd(7 * k)
maxx.rt(90)
maxx.fd(5 * k)
maxx.pd()
for i in range(1001):
    maxx.rt(90)
    maxx.fd(20 * k)
    maxx.rt(90)
    maxx.fd(36 * k)

maxx.pu()
for x in range(-40, 40):
    for y in range(-40, 40):

        maxx.goto(x * k, y * k)

        maxx.dot(3)

done()