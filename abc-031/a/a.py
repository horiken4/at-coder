# coding: utf-8

import sys


for line in sys.stdin:
    a, d = line.rstrip().split(' ')

    a = int(a)
    d = int(d)

    aup = (a + 1) * d
    dup = a * (d + 1)

    if aup >= dup:
        print aup
    else:
        print dup
