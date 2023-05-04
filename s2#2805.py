# '''
# 4 7
# 20 15 10 17
# >10
# 10 5 0 7 >> 22 즉 10크도 20보다 작아야 한다.
# 15
# 5 0 0 2
# '''
# '''
# 최대값 부터 작아지면 어떨까
# 내림으로 정렬후 큰 수부터 하나씩비교하면?
# 이분탐색
# 우선 절반 다 짜르고 크면 줄이고, 작으면 늘리고
# '''

# n, m = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))
# l = []

# def mid(mid_, f):
#     c = 0
#     for j in a:
#         if j > mid_:
#             c += j - mid_
#     if c >= m:
#         l.append(mid_)
#     if c < m:
#         if f == 1:
#             return f
#         else:
#             f = 0
#             mid(mid_//2, f)
#     else: 
#         if f == 0:
#             return f
#         else:
#             f = 1
#             mid(mid_+mid_//2, f)
# mid(max(a)//2, None)

# k = 0
# i = max(l)
# for j in a:
#     if j > max(l):
#         k += j - max(l)
# if k >= m:
#     #l을 늘려
#     while True:
#         u = 0
#         for j in a:
#             if j > i:
#                 u += j - i
#         if u <= m:
#             print(i)
#             break
#         i += 1
# elif k < m:








# for i in range(max(a),0, -1):
#     c = 0
#     for j in a:
#         if j > i:
#             c += j - i
#     if c >= m:
#         print(i)
#         break
    



#### 모범답안
import sys
#sys.stdin = open('input.txt')

n,m =map(int,sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))

le=1
ri=max(lis)

while le<=ri:
    mid = (le+ri)//2
    total= [tree-mid if tree>mid else 0 for tree in lis]
    # print(total)
    total_val = sum(total)
    # for tree in lis:
    #     if tree>mid:
    #         total+=(tree-mid)
    if total_val>=m:
        le=mid+1
    else:
        ri=mid-1

print(ri)

'''
4 8
20 15 10 17일때
처음에 mid 10 = 22의 값이 나오고
10보다 아래의 수는 값이 더 커짐으로 11부터 봐야한다.
11~20의 중간인 15의 경우 7임으로 15보다는 작아야 한다.
그래서 11~14사이의 값을 찾아야한다.
이를 반복한다.
'''