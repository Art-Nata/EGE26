from math import dist  # если функция расстояния стандартная
from turtle import *
from random import *


def dist(a, b): # если надо определитьсвою функцию
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 # формула определения функции


def centr(cl):
    cn = []
    for p in cl:
        sum_p = sum(dist(p, p1) for p1 in cl)
        cn.append([sum_p, p])
    return min(cn)[1]


A = [[], []] # кластеризация для файла А
for s in open('27_А.txt'):
    x, y = [float(d) for d in s.replace(',', '.').split()]
    if x < 10:
        A[0].append([x, y])
    else:
        A[1].append([x, y])

B = [[], [], []] # кластеризация для файла Б
for s in open('27_Б.txt'):
    x, y = [float(d) for d in s.replace(',', '.').split()]
    if y < 0 or x < -5:
        pass
    elif x > 20:
        B[0].append([x, y])
    elif y > 20:
        B[1].append([x, y])
    else:
        B[2].append([x, y])


# рисование точек кластеров с помощью черепашки
# tracer(10)
# up()
#
# for cl in B:
#     color = random(), random(), random()
#     for x, y in cl:
#         goto(x * 5, y * 5)
#         dot(2, color)
# update()

sum_centr_x = centr(A[0])[0] + centr(A[1])[0]
sum_centr_y = centr(A[0])[1] + centr(A[1])[1]
print(int(sum_centr_x * 10000), int(sum_centr_y * 10000))


min_12 = min(dist(dot1, dot2) for dot1 in B[0] for dot2 in B[1])
min_13 = min(dist(dot1, dot3) for dot1 in B[0] for dot3 in B[2])
min_23 = min(dist(dot2, dot3) for dot2 in B[1] for dot3 in B[2])
print(int(min(min_12, min_13, min_23) * 10000))



M = [18, 18]
max_B = max(dist(centr_cl, M) for centr_cl in [centr(B[i]) for i in [0, 1, 2]])

print(int(max_B * 10000))