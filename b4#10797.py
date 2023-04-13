d = list(input())
a = list(map(int, input().split(' ')))
c=0

for i in a:
    if i == int(d[-1]):
        c += 1
print(c)
