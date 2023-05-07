a, b = map(int, input().split(' '))

x = []
y = []

if (a-1)%4 == 0:   
    x.append((a-1)//4)
    x.append(0)
elif (a-2)%4 == 0:
    x.append((a-1)//4)
    x.append(1)
elif (a-3)%4 == 0:
    x.append((a-1)//4)
    x.append(2)
elif (a-4)%4 == 0:
    x.append((a-1)//4)
    x.append(3)
    
if (b-1)%4 == 0:   
    y.append((b-1)//4)
    y.append(0)
elif (b-2)%4 == 0:
    y.append((b-1)//4)
    y.append(1)
elif (b-3)%4 == 0:
    y.append((b-1)//4)
    y.append(2)
elif (b-4)%4 == 0:
    y.append((b-1)//4)
    y.append(3)

print(abs(x[0]-y[0])+abs(x[1]-y[1]))