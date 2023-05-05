n = int(input())


a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

l=[]
def tow(u):
    for i in range(len(primes)+1):
        if u == 1:
            return 
        elif u % primes[i] == 0:
            l.append(primes[i])
            tow(u//primes[i])
            break
tow(n)

[print(i)for i in sorted(l)]

# #### 모범답안
# N=int(input())
# def devide(N):
#     for i in range(2,N+1):
#         if N%i==0:
#             print(i)
#             N//=i
#             if N==1:
#                 break
#             else:
#                 devide(N)
#                 break
# devide(N)