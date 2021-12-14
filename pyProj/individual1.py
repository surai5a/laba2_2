#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    m = int(input('Input number of season(season 1 is winter): '))
    if m > 4 or m < 1:
        print("Wrong number!", file=sys.stderr)
        exit(1)
    if m == 1:
        print("Winter: Dec Jan Feb")
    elif m == 2:
        print("Spring: Mar Apr May")
    elif m == 3:
        print("Summer: Jun Jul Avg")
    elif m == 4:
        print("Fall: Sep Oct Nov")
