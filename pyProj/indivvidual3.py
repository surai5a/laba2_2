import sys
import math


def simple(k):
    flag = 1
    i = 2
    cnt = 0
    while i <= math.sqrt(k):
        if k % i == 0:
            flag = 0
            break
        i += 1
    if flag == 1:
        print(1)
    else:
        print(0)


k = int(input("Put number: "))
if k < 2:
    print("Wrong number", file=sys.stderr)
    exit(1)
simple(k)
