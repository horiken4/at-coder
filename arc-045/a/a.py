import sys

S = sys.stdin.readline().rstrip().split(' ')

outs = []
for s in S:
    if s == 'Left':
        outs.append('<')
    elif s == 'Right':
        outs.append('>')
    elif s == 'AtCoder':
        outs.append('A')

print ' '.join(outs)
