# def fibo(n):
#     global z
#     global o
#     if n == 0:
#         z += 1
#         return 0
#     elif n == 1:
#         o += 1
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

# n = int(input())
# for i in range(n):
#     z = 0
#     o = 0
#     fibo(int(input()))
#     print(z, o)

import sys
input = sys.stdin.readline
zero=[0]*42
one=[0]*42
zero[0]=1
zero[1]=0
one[0]=0
one[1]=1
t=int(input())
for i in range(t):
    n=int(input())
    for j in range(n):
        zero[j+2]=zero[j+1]+zero[j]
        one[j+2]=one[j+1]+one[j]
    print(zero[n],one[n],sep=' ')