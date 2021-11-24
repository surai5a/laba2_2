#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def triangle(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        print("Triangle cannot be built", file=sys.stderr)
        exit(1)
    if (a == b or a == c or b == c) and not (a == b == c):
        print("Triangle is isosceles")
    elif a == b == c:
        print("Triangle is equilateral")
    else:
        print("Triangle is versatile")


if __name__ == '__main__':
    print("Put 3 nums: ")
    a = int(input())
    b = int(input())
    c = int(input())
    triangle(a, b, c)

