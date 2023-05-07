# 64
# 32
# 16 16
# 16 8 
# 16 4 4
# 16 4 2 2
# 16 4 2 1 1
# 16 4 2 1 >> 23
# 64 32 16 8 4 2 1
# n 보다 작은 바로 아래 수를 고정으로 다음 수를 더해보면서 카운트

n = int(input())
r = [64, 32, 16, 8, 4, 2, 1]
c = 1

a = [i for i in r if n >= i]
for i in range(len(a)):
    if n == i:
        break
    if (a[0]+a[i]) <= n:
        a[0] = a[0]+a[i]
        c += 1
print(c)

# # 다른 방법
# x = int(input())
# num = [2 ** x for x in range(6, -1, -1)] #숫자 생성
# result = 0
# while x > 0: #x가 0이면 종료
#     for i in num:
#         if x - i >= 0: #i를 빼서 0이상이면 진행
#             x -= i #x - i >> 즉 i를 빼서 0이 되면 끝
#             result +=1
# print(result)