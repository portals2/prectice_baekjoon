# 차이가 1이면서 홀 짝 이면 붙는다. 하지만 이외의 숫에서는 싸우지 못한다.
# 20 31 홀수이면 1을 더하고 /2한다.
# 10 16
# 5  8
# 3  4

n, k, im = list(map(int, input().split(' ')))
c = 1

if k < im:
    while True:
        if (im - k == 1) and (im % 2 == 0):
            break
        if k % 2 == 1:
            k += 1
        if im % 2 == 1:
            im += 1
        k = k // 2
        im = im // 2
        c += 1
else:
    while True:
        if (k - im == 1) and (k % 2 == 0):
            break
        if k % 2 == 1:
            k += 1
        if im % 2 == 1:
            im += 1
        k = k // 2
        im = im // 2
        c += 1

print(c)
    
#### 수식에 의한 모범답안
import math

n, j, h = map(int, input().split())
result = 0

while j != h: #j와 h가 같지 않다면
    # j와 h를 모두 2씩 나누고 올려라(math.ceil)
    j = math.ceil(j/2)
    h = math.ceil(h/2)
    result += 1

print(result)