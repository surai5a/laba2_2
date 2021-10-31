import math
import sys


def biqual(a: float,
           b: float,
           c: float):
    if a == 0:
        print("Wrong number!", file=sys.stderr)

    d = math.pow(b, 2) - (4 * a * c)
    if d < 0:
        print("No roots")
        exit(0)
    elif d > 0:
        y1 = (-b + math.sqrt(d)) / (2 * a)
        y2 = (-b - math.sqrt(d)) / (2 * a)
        if y1 >= 0:
            x1 = math.sqrt(y1)
            x2 = -(math.sqrt(y1))
        elif y2 >= 0:
            x3 = math.sqrt(y2)
            x4 = -(math.sqrt(y2))
        else:
            print("no roots")
            exit(0)
        if y1 >= 0 and y2 >= 0:
            print(f"x1 = {x1}\nx2 = {x2}\nx3 = {x3}\nx4 = {x4}")
        elif y1 >=0:
            print(f"x1 = {x1}\nx2 = {x2}")
        elif y2 >= 0:
            print(f"x3 = {x3}\nx4 = {x4}")
    elif d == 0:
        y = (-b) / (2 * a)
        if y > 0:
            x1 = math.sqrt(y)
            x2 = -(math.sqrt(y))
            print(f"x1 = {x1}\nx2 = {x2}")
        else:
            print("No roots")
        exit(0)


a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

biqual(a, b, c)
