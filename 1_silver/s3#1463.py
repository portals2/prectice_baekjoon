# 1에서 부터 2나 3을 곱하고 1을 더하는 수로 나타낸다.
# 10 > 1 + 3*3 >>> 즉 3번 // 11 > 1+ 3*3 +1 >> 즉 4번
# 100 > 1 + 3*33 >> 즉 33번
# 5 > 1 + 3 + 1
# 5 -1 4 /2 2 /2 1 > 3 // 5 -1 4 -1 3 /3 1 > 3

# 근데 결국 x에서 1을 뺴고 0을 만드는 작업

x = int(input())
c = 0

if (x & (x - 1)):
    while x != 1:
        if x % 3 == 0:
            x = x // 3
            c += 1
        else:
            x = x - 1
            c += 1
    print(c)
else:
    while x != 1:
        x = x // 2
        c += 1
    print(c)

#### 모범 답안 https://bio-info.tistory.com/159
x=int(input()) # 수 입력받기
d=[0]*(x+1) # 1-based
for i in range(2,x+1): # 2부터 x까지 반복
    d[i]=d[i-1]+1 # 1을 빼는 연산 -> 1회 진행
    if i%2==0: # 2로 나누어 떨어질 때, 2로 나누는 연산
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0: # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        d[i]=min(d[i],d[i//3]+1)
print(d[x])