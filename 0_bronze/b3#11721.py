a = list(input())

while a:
    print(''.join(a[:10]))
    del a[:10]