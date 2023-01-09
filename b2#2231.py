# 198 >> 198+1+9+8 = 216 으로 216을 입력했을 때 198을 출력하라

num = int(input())

re = 0

for i in range(num):
    if num < 0: continue
    if num == i + sum(list(map(int, str(i)))):
        re += i
        break

print(re)
  
### sys가 뭐야?
# import sys


# N = int(sys.stdin.readline())
# digit = len(str(N))
# for num in range(N - 9 * digit, N):
#     if num < 0: continue
#     lists = list(str(num))
#     if num + sum(map(int, lists)) == N:
#         print(num)
#         exit(0)
# print(0)  