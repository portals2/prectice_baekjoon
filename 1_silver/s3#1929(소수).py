# import sys
# input=sys.stdin.readline

# x, y = map(int, input().split(' '))

# a = [False,False] + [True]*(y-1)
# primes=[]

# for i in range(1,y+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(2*i, y+1, i):
#         a[j] = False
# for i in primes:
#     if i >= x:
#         print(i)

def sosu(N):
    # check=1
    if N==1:
        return 0
    for j in range(2, int(N**(1/2))+1):
        if N%j==0:
            # check=0
            return 0
    else:
        return 1


a, b = map(int,input().split())
for i in range(a,b+1):
    if sosu(i)==1:
        print(i)