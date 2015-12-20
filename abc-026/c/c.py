# coding: utf-8

import sys
import math

N = int(sys.stdin.readline().rstrip())
B = []
for line in sys.stdin:
    B.append(int(line.rstrip()))

B = map(lambda x: x - 1, B)

def sarary(i):
    mi = sys.maxint
    ma = -1
    c = 0

    for j, b in enumerate(B):
        if b == i:
            c += 1
            s = sarary(j + 1)
            if s < mi:
                mi = s
            if s > ma:
                ma = s

    if c == 0:
        return 1

    return ma + mi + 1

print sarary(0)


