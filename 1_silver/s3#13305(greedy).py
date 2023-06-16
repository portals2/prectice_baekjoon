# 첫번쨰 도시보다 싼값의 도시가 있다면 
# 그 도시까지의 기름을 충전한다.
# 이후 더이상 싼 도시가 없다면
# 남은 거리의 기름을 모두 충전한다.
# 마지막 도시는 제외한다.

## 이게 왜 그리디 문제일까?

city = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

chip_c = price[0]
cost = 0


for i in range(1, city-1):
    if price[i] < chip_c:
        cost += chip_c* sum(km[i-1:i]) # 21번 라인과 같은 코드
        chip_c = price[i]
    else:
        cost += chip_c* km[i-1]

cost += chip_c* km[-1]

print(cost)

#### 모범답안
import sys
input=sys.stdin.readline

N=int(input())
D = list(map(int,input().split()))
C = list(map(int,input().split()))
result = 0

c = C[0]
# 나는 도시를 기준으로 생각했다.
# 여기는 distance를 기준으로 생각 헀다.
# 어차피 0번째 도시를 출발 할 때는 0번째 거리의 값을 가져와야 하니까
for i in range(N - 1):
    if c > C[i]:
        c = C[i] # 싼가격이 나오면 고정
    result += c * D[i] # 도시를 이동할 때마다 가격을 지불

print(result)
