import sys


vs = sys.stdin.readline().rstrip().split(' ')
vs = map(int, vs)
a, b, c, d = vs

wr_taka = float(b) / a
wr_aoki = float(d) / c

if wr_taka > wr_aoki:
    print 'TAKAHASHI'
elif wr_taka < wr_aoki:
    print 'AOKI'
else:
    print 'DRAW'
