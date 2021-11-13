import math
import sys


def triangle(a, b, c):
    if a + b < c or b + c < a or a + c < b:
        print("Triangle cannot be built", file=sys.stderr)
        exit(1)
    if (a == b or a == c or b == c) and not (a == b == c):
        print("Triangle is isosceles")
    elif a == b == c:
        print("Triangle is equilateral")
    else:
        print("Triangle is versatile")


a, b, c = (c for c in input("Put a b c: ") if c != ' ')
triangle(a, b, c)

