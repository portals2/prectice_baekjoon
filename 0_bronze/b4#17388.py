a,b,c =map(int, input().split(' '))

if a+b+c >= 100:
    print('OK')
else:
    if min(a,b,c) == a:
        print('Soongsil')
    if min(a,b,c) == b:
        print('Korea')
    if min(a,b,c) == c:
        print('Hanyang')