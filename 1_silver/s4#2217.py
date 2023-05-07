# # w의 무게를 구하는 것
# # 가장 작은 수의 최대 무게를 기준으로 구하고 
# # if 만약 이것이 가장 큰 무게보다 작다면 
# # 가장 작은 수를 제외하고 다시 구해본다.
# # 큰 무게보다 w가 높다면 그것이 최댓값

# n = int(input())

# w = []

# for i in range(n):
#     w.append(int(input()))

# w.sort()

# for i in range(n):
#     s = w[i]*n
#     if w[i]*n >= max(w):
#         print(w[i]*n)
#         break
#     elif w[i+1]*(n-(i+1)) >= max(w):
#         print(w[i+1]*(n-(i+1)))
#         break
#     else:
#         pass

####모범답안 낮은 로프부터 탐색####
import sys
N = int(input())
arr=[] 
result =0

for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

for i in range(N):
    result =max((N-i)*arr[i],result)

print(result)



####모범답안 reverse이용해서 꺼꾸로 탐색####
import sys
N = int(sys.stdin.readline())
K = [int(sys.stdin.readline())for i in range(N)]
K.sort(reverse=True)
max = 0

for i in range(N):
    if K[i] * (i+1) >max:
        max = K[i] * (i+1)
else:
    max = max

print(max)