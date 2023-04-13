n = int(input())

a = {}

for i in range(n):
    b = input()
    if b not in a:
        a[b] = 1
    else:
        a[b] += 1
aa = sorted(a.items(), key=lambda x: x[1])
l = []
for key, v in aa:
    if v == max(a.values()):
        l.append(key)
print(sorted(l)[0])

#### 신기한 답안
n,*a=open(0)
print(max(sorted(a),key=a.count))