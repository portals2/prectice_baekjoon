'''
땅의 배열을 한줄로 늘려도 상관없다. 
모두 같은 숫자면 되니까

평균과 각 숫자의 차의 전체합이 0이면 평균
'''
'''
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split(' '))

l = []
for i in range(n):
    l+=(list(map(int, input().split(' '))))

max = max(l)
min = min(l)
x = [0] * len(l)
l_ = []
if n == 1 and m == 1:
    print(0, l[0])
else:
    while max != min-1:
        c = 0
        for i in range(len(l)):
            x[i] = l[i] - max

        if sum(x)+b >= 0:
            for i in x:
                if i > 0:
                    b += i
                    c += i*2
                else:
                    c += abs(i)
            l_.append([c, max])
            max = max-1
        else:
            max = max-1

    ans = sorted(l_, key= lambda x : (x[0], -x[1]))[0]
    for i in ans:
        print(i, end=' ')


#### 파이썬으로 해결한 (used 코드Counter)
from collections import Counter
from sys import stdin
input = stdin.readline
n, m, b = map(int, input().split())
land = Counter()
for i in range(n):
    land.update(map(int, input().split()))
ans = [10e9, 0]
for h in range(min(land),max(land)+1):
    bag = b
    sec = 0
    for height, cnt in land.items():
        if height > h:
            sec += (height - h)*2 * cnt
            bag += (height - h) * cnt
        else:
            sec += (h - height) * cnt
            bag -= (h - height) * cnt
    if bag >= 0:
        if sec <= ans[0]:
            ans[0] = sec
            ans[1] = h
print(*ans)
'''

#### 파이썬 해결 코드
I=lambda:map(int,input().split())
n,m,b=I()
l=[]

for i in range(n):l.extend(I())
dic={}
#각 칸의 높이를 key로 얼마나있는지 velue로 나타냄
for i in l:
    if i not in dic:
        dic[i]=1 
    else:
        dic[i]+=1
rt=8**9
rh=0

for i in range(min(l),max(l)+1): #낮은 곳부터 높은 곳으로
    t=0 #시간
    tb=b # 가진 블록
    for j in dic:
        q=dic.get(j)
        if j>i: #i=0 i보다 높은지 확인
            t+=(j-i)*q*2 # i층을 뺸 j층을 부시는 시간
            tb+=(j-i)*q # 부신 블럭을 채우기
        else:
            t+=(i-j)*q # j가 i층 보다 낮다면 블럭 놓기 시간
            tb-=(i-j)*q #아이템이 빠져나간다.
    if tb>=0: # 가진 블록이 있다. >> 아직 더 쌓을 수 있다.
        if t<=rt: # rt를 검사해서 최소 시간을 확정한다. 만약 같다면, 더 높은 층과 시간을 알 수 있다.
            rt=t
            rh=i
print(rt,rh)