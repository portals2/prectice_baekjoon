# 64
# 32
# 16 16
# 16 8 
# 16 4 4
# 16 4 2 2
# 16 4 2 1 1
# 16 4 2 1 >> 23

a = list(map(str, input()))
d = []

if (a[0] == '-') or (a[0] == '='):
    d.append(0)
for i in range(1, len(a)):
    if (a[i] == '='):
        if (a[i-1] == 'z') and (a[i-2] == 'd'):
            d.append(i-1)
            d.append(i)
            a[i-2] =a[i-2] + a[i-1] + a[i]
        elif (a[i-1] == 'c') or  (a[i-1] == 's') or  (a[i-1] == 'z'):
            d.append(i)
            a[i-1] = a[i-1] + a[i]
        else:
            d.append(i)
    elif (a[i] == '-'):
        if (a[i-1] == 'c') or (a[i-1] == 'd'):
            d.append(i)
            a[i-1] = a[i-1] + a[i]
        else:
            d.append(i)
    elif (a[i] == 'j') and ((a[i-1] == 'l') or (a[i-1] == 'n')):
        d.append(i)
        a[i-1] = a[i-1] + a[i]

d.sort(reverse=True)
for i in d:
    del(a[i])
print(len(a))