import sys
input=sys.stdin.readline

n = int(input())
a = []

for i in range(n): # 0~ n
    a.append(int(input()))

print(sum(a)-(len(a)-1))
