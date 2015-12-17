import sys

N = int(sys.stdin.readline().rstrip())


def enum(pw):
    if len(pw) == N:
        print pw
        return

    alpha = ['a', 'b', 'c']
    for a in alpha:
        enum(pw + a)

enum('')
