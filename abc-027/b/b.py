import sys

N = int(sys.stdin.readline().rstrip())
A = map(int, sys.stdin.readline().rstrip().split(' '))

if 0 != sum(A) % N:
    print -1
    sys.exit(0)

fa = A[0]
if all(map(lambda x: fa == x, A[1:])):
    print 0
    sys.exit(0)


