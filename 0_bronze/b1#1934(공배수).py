# import sys

# t = int(sys.stdin.readline())

# for _ in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     answer = 1
#     num = 2
#     while (num <= a and num <= b):
#         if a % num == 0 and b % num == 0:
#             answer *= num
#             a //= num
#             b //= num
#         else:
#             num += 1
        
#     answer *= (a*b)
#     print(answer)



####
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    x,y=map(int,sys.stdin.readline().split())
    k = 0
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            k = i
    print(x*y//k)
