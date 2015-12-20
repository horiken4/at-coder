import sys
import math

N = int(sys.stdin.readline().rstrip())
R = []
for line in sys.stdin:
    R.append(int(line.rstrip()))
R.sort(reverse=True)

s = 0
for i, _ in enumerate(R):
    if i % 2 == 0:
        s += R[i] ** 2
    else:
        s -= R[i] ** 2

print s * math.pi



