import sys

S = list(sys.stdin.readline().rstrip())


hist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}

for a in S:
    hist[a] += 1

print '{0} {1} {2} {3} {4} {5}'.format(hist['A'], hist['B'], hist['C'], hist['D'], hist['E'], hist['F'])
