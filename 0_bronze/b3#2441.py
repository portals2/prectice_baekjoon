n = int(input())
s = ""

for i in range(n):
    print(s, end='')
    for j in range(n):
        print('*',end='')
    print("")
    n -= 1
    s += " "