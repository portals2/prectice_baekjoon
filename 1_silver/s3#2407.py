# # nCm 
# # n 부터 m-1까지 top-down 방식


# n,m = map(int, input().split())

# # 100-6 = 94
# n_ = 1
# r_ = 1
# nr_ = 1

# for i in range(2, n+1):
#     n_ *= i

# for i in range(2, m+1):
#     r_ *= i

# for i in range(2, (n-m)+2):
#     nr_ *= i

# print(n_ // r_*nr_)


n,k = map(int, input().split())

def fac(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

print(int(fac(n)//(fac(k)*fac(n-k))))