n = int(input())
num = list(map(int, input().split(' ')))
f = int(input())
count = 0

for i in range(n):
    if num[i] == f:
        count += 1
print(count)