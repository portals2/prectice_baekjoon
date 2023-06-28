

n,m = map(int,input().split())
num = list(map(int, input().split()))

l = num[:n]
r = num[n:]
c= 0

num = []

for i in range(1, 6):
    num.append(r.count(i))

for i in l:
    c += (sum(num) - num[i-1])%15746

print(c)