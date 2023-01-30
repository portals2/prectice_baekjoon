n = int(input())

i = 0
a = 5
b = 1
x,y,z = 0,0,0
while b >= 0:
    if b % 3 == 0:
        x= (i+(b//3))
    b = n - a
    i += 1
    a += 5
if n % 3 == 0:
    y =(n // 3)
if (b <= 0) or (n==0):
    z =(-1)

if x > 0:
    print(x)
elif y > 0:
    print(y)
else:
    print(z)

    
##################모범답안
# N = int(input())
# cnt = 0
# if N%5 == 0:
#     print(N//5)
# else:
#     while N >= 0:
#         N -= 3
#         cnt += 1
#         if N % 5 == 0:
#             print(N//5 + cnt)
#             break
#     else:
#         print(-1)