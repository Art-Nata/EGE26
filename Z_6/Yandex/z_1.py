"""Черепахе был дан для исполнения следующий алгоритм:

Направо 30 Вперед 45 Налево 120 Вперед 25

Изображение какой десятичной цифры является результатом алгоритма?"""


from turtle import *


#tracer(0)
maxx = Turtle()
screensize(1000, 1000)
maxx.pensize(3)
maxx.color('red')

k = 10


maxx.home()

maxx.rt(30)
maxx.fd(45 * k)
maxx.lt(120)
maxx.fd(25 * k)

done()