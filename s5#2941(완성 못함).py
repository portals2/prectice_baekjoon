# a= ['a','b','c','d']

# a[1] = a[1]+a[2]
# del(a[2])
# print(a)

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
        elif (a[i-1] == 'c') and  (a[i-1] == 's') and  (a[i-1] == 'z'):
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
    elif (a[i-1] == 'l') or (a[i-1] == 'n') and (a[i] == 'j'):
        d.append(i)
        a[i-1] = a[i-1] + a[i]

d.sort(reverse=True)
for i in d:
    del(a[i])
print(len(a))
print(a)

# for i in a:
#     if (i == '=') or (i == '-'):


    # elif (a[i-1] == 'z') and (a[i-2] == 'd') and (a[i] == '=') or (a[i] == '-'):
    #     d.append(i-1)
    #     d.append(i)
    #     a[i-2] =a[i-2] + a[i-1] + a[i]