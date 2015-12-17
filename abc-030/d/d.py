import sys

N, a = map(int, sys.stdin.readline().rstrip().split(' '))
a -= 1
k = int(sys.stdin.readline().rstrip())
B = map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split(' '))

"""
print 'a:', a
print 'k:', k
print 'B:', B
"""

# find cycle
find = a
path = []
visited = set()
cycle_begin = -1

while find not in visited:
    path.append(find)
    visited.add(find)
    find = B[find]
cycle_begin = path.index(find)
cycle_path = path[cycle_begin:]

"""
print 'path:', path
print 'cycle_begin:', cycle_begin
print 'cycle_path:', cycle_path
"""

if k >= len(path):
    k -= cycle_begin
    step = k % len(cycle_path)
    print cycle_path[step] + 1
else:
    print path[k] + 1
