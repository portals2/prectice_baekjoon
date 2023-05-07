n = int(input())
a = map(int, input().split(' '))
m= int(input())
w = map(int, input().split(' '))

count={}
for i in a:
    if count.keys() != i:
        count[i] = 0
for j in w:
    if j in count:
        print(1)
        count[j] += 1
    else:
        print(0)
print(count)