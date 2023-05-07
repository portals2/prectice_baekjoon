n = int(input())    

l = [i for i in range(1, n+1)]

for i in range(1, n*2):
    if i % 2 != 0:
        print(l[0])
        l.pop(0)
    else:
        l.append(l[0])
        l.pop(0)


#### 짧은 답안
queue=[]
n=int(input())
for i in range(1,n+1):
    queue.append(i)
while queue!=[]:
    print(str(queue.pop(0)),end=' ')
    if queue!=[]:queue.append(queue.pop(0))