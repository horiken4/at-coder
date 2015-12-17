import sys

c = 0
for line in sys.stdin:
    if 'r' in line:
        c += 1

print c
