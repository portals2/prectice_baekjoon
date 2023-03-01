import math 

n = list(map(str, input()))

num = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for i in n:
    if i == '9':
        num['6'] += 1
    else:
        num[i] += 1


if (max(num.values()) == num['6']):
    num['6'] = math.ceil(num['6']/2)
    print(max(num.values()))
    
else:
    print(max(num.values()))

