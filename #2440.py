n = int(input())

k=n
for i in range(n):
    for j in range(k):
        print('*', end='')
    print('')
    k -= 1
    
