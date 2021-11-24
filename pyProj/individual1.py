#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def season(mon):
    if mon > 4 or mon < 1:
        print("Wrong number!", file=sys.stderr)
        exit(1)
    months = [
        {1: 'Winter: Dec Jan Feb'},
        {2: 'Spring: Mar Apr May'},
        {3: 'Summer: Jun Jul Avg'},
        {4: 'Fall: Sep Oct Nov'}
    ]
    print(months[mon - 1])


if __name__ == '__main__':
    m = int(input('Input number of season(season 1 is winter): '))
    season(m)
