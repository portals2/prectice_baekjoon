n = int(input())   
c = 0
s = 0

a = list(map(int, input().split()))

a.sort()
for i in a:
    c += i
    s += c
print(s)
