import sys
input=sys.stdin.readline

for i in range(3):
    s = 0
    n = int(input())
    for j in range(n):
        s += int(input())
    if s > 0:
        print('+')
    elif s < 0:
        print('-')
    else:
        print('0')