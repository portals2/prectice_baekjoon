how_num = int(input())


for i in range(how_num):
    a = ""
    n, alpha = list(map(str, input().split(' ')))
    for j in list(alpha):
        a += j * int(n)
    print(a)