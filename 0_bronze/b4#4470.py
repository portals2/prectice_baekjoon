import sys
input=sys.stdin.readline

n = int(input())

for i in range(n):
    a = input()
    print('{0}. {1}'.format((i+1), a), end='')