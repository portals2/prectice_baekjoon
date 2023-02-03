# 소수 pq를 곱한 값, 크기 제한값
# 1. 특정값을 받았을 떄 두개의 소수로 
# 나눌 수 있어야 한다. 

# 해답 : p가 k이하의 수로 나누어지면
# 안된다. >> p가 소수의 곱이기 때문에
# 나누어서 떨어지는 수 ㄴ또한 소수이다.

# import sys
# input=sys.stdin.readline
# n,m = map(int, input().split(' '))

# a = [False,False] + [True]*(n-1)
# primes=[]

# for i in range(2,n+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False

# for i in range(len(primes)):
#     for j in range(i, len(primes)):
#         if primes[i] * primes[j] == n:
#             if (primes[i] <= m) or (primes[j] <= m):
#                 print('BAD', primes[i])
#             else:
#                 print('GOOD')
            
p, k = map(int, input().split())

prime = [False, False] + [True] * (k-2)
for i in range(2, int(k**0.5)+1):
    if prime[i]:
        for j in range(i+i, k, i):
            if prime[j]:
                prime[j] = False
                
flag = True
for i in range(2, k):
    if prime[i]:
        if p % i == 0:
            flag = False
            break
            
if flag:
    print('GOOD')
else:
    print('BAD', i)