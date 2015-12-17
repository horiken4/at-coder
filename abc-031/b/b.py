# coding: utf-8

import sys


l, h = sys.stdin.readline().rstrip().split(' ')
l = int(l)
h = int(h)

n = sys.stdin.readline().rstrip()
n = int(n)

alist = []
for i in range(n):
    alist.append(int(sys.stdin.readline().rstrip()))


for a in alist:
    if a <= l:
        print l - a
    elif l <= a <= h:
        print 0
    elif h <= a:
        print -1
