# coding: utf-8

import sys
import math

A, B, C = map(float, sys.stdin.readline().rstrip().split(' '))

def f(t):
    return A * t + B * math.sin(C * t * math.pi)

def err(t):
    return abs(f(t) - 100)

tl = 0
tu = 500
tm = (tl + tu) / 2.0
while err(tm) > 10e-11:
    tm = (tl + tu) / 2.0
    if f(tm) < 100:
        tl = tm
    else:
        tu = tm
    #print err(tm)

#print err(tm)
print tm
#print f(tm)



