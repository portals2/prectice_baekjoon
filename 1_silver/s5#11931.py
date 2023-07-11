import sys
input = sys.stdin.readline
n = int(input())

a = []

for i in range(n):
    a.append(int(input()))

for i in sorted(a, reverse=True):
    print(i)