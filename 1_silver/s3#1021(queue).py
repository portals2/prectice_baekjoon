'''
10 3 // 123
1234567890
2 345678901 // 1
9 01345678 // 3
5 6780134 // 4
n/2 보다 크면 오른쪽에서 작으면 윈쪽에서 카운트
'''

n, m = map(int, input().split(' '))
m_ = list(map(int, input().split(' ')))

l = [i for i in range(1, n+1)]
c = 0
lr = 0

while True:
    mid = len(l)//2
    if (l.index(m_[c]) <= mid) and (m_[c] != l[0]):
        l.append(l.pop(0))
        lr += 1
    elif (l.index(m_[c]) > mid) and (m_[c] != l[0]):
        l.insert(0, l.pop())
        lr += 1
    else:
        if m_[-1] == l[0]:
            break
        l.pop(0)
        c += 1

print(lr)

#### 한번에 옮겨 붙이기
# n,m=map(int,input().split())
# que=[i for i in range(n)]
# info=list(map(lambda x:int(x)-1,input().split()))
# cnt=0
# for i in info:
#     p=que.index(i) #목표에 인덱스를 확인
#     if p<=len(que)-p-1: # 반이 안넘으면 p를 바로 더함
#                         # 앞에서 p번째까지 움직이는 횟수
#         cnt+=p
#     else:
#         cnt+=len(que)-p # 반이 넘으면 p를 빼서 더함
#                         # 뒤에서 p번째까지 움직이는 횟수
#     que=que[p:]+que[:p] # p를 기준으로 앞뒤를 다 붙임
#     que.pop(0)
# print(cnt)