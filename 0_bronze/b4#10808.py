a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
s = str(input())

for i in s:
    a[ord(i)-97] += 1
 
for i in a:
    print(i, end=' ')
