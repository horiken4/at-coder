# coding: utf-8

import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

ranges = []
for line in sys.stdin:
    r = map(lambda x: int(x) - 1, line.rstrip().split(' '))
    ranges.append(r)


# imos法で各教室がいくつの区間に含まれているか調べる
cover = [0] * (N + 1)
for r in ranges:
    cover[r[0]] += 1
    cover[r[1] + 1] -= 1
for i in range(1, len(cover)):
    cover[i] += cover[i - 1]
cover = cover[:-1]

# すべて教室が2以上の区間に含まれている区間(さぼれる区間)を列挙
cover = map(lambda x: 0 if x > 1 else 1, cover)

for i in range(1, len(cover)):
    cover[i] += cover[i - 1]
cover.append(0)

can_loaf_ranges = []
for i, r in enumerate(ranges):
    num_only_cover_rooms = cover[r[1]] - cover[r[0] - 1]
    #print num_only_cover_rooms
    if num_only_cover_rooms == 0:
        can_loaf_ranges.append(i)

print len(can_loaf_ranges)
for ri in can_loaf_ranges:
    print ri + 1






