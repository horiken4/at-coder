# coding: utf-8

import sys


def calc_score(S, i, j):
    if i < j:
        T = S[i:j + 1]
    else:
        T = S[j:i + 1]

    taka = 0
    aoki = 0
    for k, a in enumerate(T):
        if (k + 1) % 2 == 0:
            aoki += a
        else:
            taka += a

    return taka, aoki


N = int(sys.stdin.readline().rstrip())

S = sys.stdin.readline().rstrip().split(' ')
S = map(int, S)

taka_max = -sys.maxint - 1
for i in range(len(S)):

    aoki_max = -sys.maxint - 1
    aoki_choice = 0
    for j in range(len(S)):
        if i == j:
            continue

        taka, aoki = calc_score(S, i, j)

        if aoki > aoki_max:
            aoki_max = aoki
            aoki_choice = j

    taka, aoki = calc_score(S, i, aoki_choice)

    if taka > taka_max:
        taka_max = taka

print taka_max
