a = []
k =200
j = 0
for i in range(1, 20): #19개
    a.append(i)
a.sort(reverse=True)

while sum(a) < k:
    a[j] += 1
    j += 1
    
print(a)