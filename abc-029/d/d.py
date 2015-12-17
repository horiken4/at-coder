import sys

N = int(sys.stdin.readline().rstrip())
N += 1

cnt = 0
for n in range(1, 10):
    a = (N / 10 ** n) * 10 ** (n - 1)

    b = N % 10 ** n

    c = 0
    lo = 10 ** (n - 1)
    up = 2 * (10 ** (n - 1))
    if lo <= b < up:
        c = b - lo
    if up <= b:
        c = up - lo

    #print 'a:', a, 'c:', c
    cnt += a + c

print cnt
