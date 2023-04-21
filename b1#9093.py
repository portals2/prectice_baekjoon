n = int(input())

for i in range(n):
    a= input()
    r_a = ''
    for i in a:
        r_a = i + r_a

    aa = r_a.split(' ')
    for i in range(1, len(aa)+1):
        print(aa[-i], end=' ')
    print('')
