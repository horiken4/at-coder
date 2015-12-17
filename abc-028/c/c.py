import sys

V = map(int, sys.stdin.readline().rstrip().split(' '))

vs = set()
for i in range(len(V)):
    for j in range(len(V)):
        if i == j:
            continue
        for k in range(len(V)):
            if i == k or j == k:
                continue
            vs.add(V[i] + V[j] + V[k])


vs = list(vs)
vs.sort()

print vs[-3]
