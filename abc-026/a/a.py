import sys

A = int(sys.stdin.readline().rstrip())

m = 0
for x in range(A):
    for y in range(A):
        if x + y == A:
            if m < x * y:
                m = x * y

print m



