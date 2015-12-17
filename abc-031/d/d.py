# coding: utf-8

import sys

K, N = sys.stdin.readline().rstrip().split(' ')
K = int(K)
N = int(N)

V = []
W = ''

for i in range(N):
    v, w = sys.stdin.readline().rstrip().split(' ')

    v = map(lambda x: int(x) - 1, list(v))
    V.extend(v)

    W += w


def solve():
    s_lens = []
    s_list = select_s_len(0, s_lens)

    #print s_list
    for _, v in s_list.items():
        print v


def is_len_valid(s_lens):
    total_len = 0
    for v in V:
        total_len += s_lens[v]

    if total_len == len(W):
        return True

    return False


def split_to_s_list(s_lens):
    s_list = {}
    b = 0
    for v in V:
        l = s_lens[v]
        s_list[v] = W[b:b + l]
        b += l

        if K == len(s_list):
            break

    return s_list


def is_text_valid(s_list):
    reconst_W = ''
    for v in V:
        reconst_W += s_list[v]

    if reconst_W == W:
        return True

    return False


def select_s_len(s_idx, s_lens):
    if s_idx == K:
        if not is_len_valid(s_lens):
            return None

        s_list = split_to_s_list(s_lens)
        if is_text_valid(s_list):
            return s_list

        return None

    for l in range(1, 3 + 1):
        lens = s_lens[:]
        lens.append(l)
        s_list = select_s_len(s_idx + 1, lens)
        if s_list is not None:
            return s_list


solve()
