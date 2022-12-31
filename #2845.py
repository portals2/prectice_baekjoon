man, m2 = map(int, input().split(' '))
n1, n2, n3, n4, n5 = map(int, input().split(' '))

man_g = man * m2

for i in n1, n2, n3, n4, n5:
    print(i - man_g, end=' ')