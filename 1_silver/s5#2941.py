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

# for i in a:
#     if (i == '=') or (i == '-'):

# # 완벽한 모범 답안
# # str을 분리하지 않고 해당 글자를 비교해서 하나씩 빼주었다.
# n = input()
# cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=', 'z=']
# count = len(n)
# for x in cro:
#     count -= n.count(x)
# print(count)

