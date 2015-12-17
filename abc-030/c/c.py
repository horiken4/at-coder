import sys
import bisect

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
X, Y = map(int, sys.stdin.readline().rstrip().split(' '))

A = map(int, sys.stdin.readline().rstrip().split(' '))
B = map(int, sys.stdin.readline().rstrip().split(' '))

rt = 0
time = 0
turn = 0
loop = True

while loop:
    if turn % 2 == 0:
        if A[-1] < time:
            loop = False
            break

        time = A[bisect.bisect_left(A, time)]
        board = time

        time += X
        arrive = time

        #print 'A({0})->B({1})'.format(board, arrive)

    else:
        if B[-1] < time:
            loop = False
            break
        time = B[bisect.bisect_left(B, time)]
        board = time

        time += Y
        arrive = time

        #print 'B({0})->A({1})'.format(board, arrive)

        rt += 1

    turn += 1

print rt
