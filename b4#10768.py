a = int(input())
b = int(input())

if a < 2:
    print('Before')
elif a > 2:
    print('After')
else:
    if b > 18:
        print('After')
    elif b < 18:
        print('Before')
    else:
        print('Special')