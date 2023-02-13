n = int(input())

s = n-1

for i in range(1,n):
    print(" "*s, end='')
    print('*'*(2*i-1))
    s -= 1

s = 0

for i in range(1,n+1):
    print(" "*s, end='')
    print('*'*((2*n+1-1)-(2*i-1)))
    s += 1