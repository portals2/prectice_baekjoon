'''
땅의 배열을 한줄로 늘려도 상관없다. 
모두 같은 숫자면 되니까

평균과 각 숫자의 차의 전체합이 0이면 평균
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


#### 파이썬으로 해결한 코드Counter
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


#### 파이썬 해결 코드
I=lambda:map(int,input().split())
n,m,b=I()
l=[]
for i in range(n):l.extend(I())
dic={}
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
rt=8**9
rh=0
for i in range(min(l),max(l)+1):
    t=0
    tb=b
    for j in dic:
        q=dic.get(j)
        if j>i:
            t+=(j-i)*q*2
            tb+=(j-i)*q
        else:
            t+=(i-j)*q
            tb-=(i-j)*q
    if tb>=0:
        if t<=rt:
            rt=t
            rh=i
print(rt,rh)