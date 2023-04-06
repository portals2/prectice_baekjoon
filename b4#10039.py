a = []

for i in range(5):
    k = (int(input()))
    if k < 40:
        a.append(40)
    else:
        a.append(k)


print(sum(a)//5)