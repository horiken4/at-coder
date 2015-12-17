import sys

N, K = map(int, sys.stdin.readline().rstrip().split(' '))

print (float(N - K) * (K - 1) * 6 + (N - 1) * 3 + 1) / N ** 3
