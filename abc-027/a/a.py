import sys

L = map(int, sys.stdin.readline().rstrip().split(' '))

a = {}
for l in L:
    if l not in a:
        a[l] = 0
    a[l] += 1

ls = a.keys()
if len(ls) == 1:
    print ls[0]
else:
    if a[ls[0]] < a[ls[1]]:
        print ls[0]
    else:
        print ls[1]
