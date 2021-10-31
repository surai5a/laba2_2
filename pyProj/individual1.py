# -*- coding: utf-8 -*-


def month(m):
    import sys
    if m > 12 or m < 1:
        print("Wrong number!", file=sys.stderr)
        exit(1)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i in months:
        if months.index(i) == (m - 1):
            print('Month is', i)


m = int(input('Input number of month: '))
month(m)
