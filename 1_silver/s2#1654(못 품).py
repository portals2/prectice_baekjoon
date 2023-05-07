# # 주어진 랜선 중에서 가장 작은 랜선을 반으로 잘라가면서, 
# # 필요 갯수에 도달한다. 이때 남는 선의 길이가 가장 짧아야 한다.

# # 802 4 / 2
# # 743 3 / 143
# # 457 2 / 57
# # 539 2 / 139 >> 200 으로 짤라서 남은 가장 짧은 선들 

'''
못푼 이유(23.02.17.)
이진 탐색의 내용은 어느 정도 이해했지만
나누는 범위를 설정함에 있어서 가장 작은
랜선을 가지고 설정하면 된다고 생각했음
if 작은 랜선이 충분히 크다면 상관 없지만
1인 경우 그대로 종료 되어 버리기 때문에
모든 case를 만족하지 못하고, 코드가 번잡해짐
'''

# import sys
# input=sys.stdin.readline

# k, n = map(int, input().split())
# a=[]
# ans=[]

# for i in range(k):
#     a.append(int(input()))

# mins = min(a)
# p_min = 0
# while True:
#     c=0
#     for i in range(k):
#         c += a[i]//mins
#     if c >= n:
#         print(mins)
#         break
#     elif c > n:
#         mins = (mins+p_min) // 2
#     elif c < n:
#         p_min = mins
#         mins = mins // 2
        

# for i in range(mins, p_min+2):
#     c= 0
#     for j in range(k):
#         c += a[j]//i
#     if c >= n:
#         ans.append(i)

# print(ans)

#모범 답안#########################################
import sys

k, n = map(int, sys.stdin.readline().split())
arr = []

for i in range(k):
    arr.append(int(input()))

start = 1 
end = max(arr)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += arr[i] // mid
    if cnt >= n: #자른 선이 n보다 크거나 같다면
        start = mid + 1 #중간에서 +1이 start
    else: #자른 선이 n보다 작거나 같다면
        end = mid - 1 #중간에서 -1이 end
print(end)
