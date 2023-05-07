n = int(input())

p = map(int, input().split(' '))
con=0

n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for i in p:
    if i in primes:
        con +=1
    
print(con)

# #에라토스테네스의 체 뿌셔버리기
# n=1000
# a = [False,False] + [True]*(n-1) # 0과 1은 소수가 아니다.
# primes=[]

# for i in range(2,n+1): #0 ~ 1000
#   if a[i]: #a[i]의 자리가 True면 작동
#     primes.append(i)
#     for j in range(2*i, n+1, i): # i를 제외한 i배수를 Flase처리하여 소수를 구분
#         a[j] = False
# print(primes)

## 모범 답안 (내가 생각 했던 for으로)
# n = int(input())
# numbers = map(int, input().split())
# sosu = 0
# for num in numbers:
#     error = 0
#     if num > 1 :
#         for i in range(2, num):  # 2부터 n-1까지
#             if num % i == 0:
#                 error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
#         if error == 0:
#             sosu += 1  # error가 없으면 소수.
# print(sosu)