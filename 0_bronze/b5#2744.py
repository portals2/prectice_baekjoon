l = list(input())

for i in range(len(l)):
    if ord(l[i]) <= 90:
        l[i] = l[i].lower()
    else:
        l[i] = l[i].upper()
        
for i in range(len(l)):
    print(l[i], end='')