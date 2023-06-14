n, k = map(int, input().split())

c = 0

while n != 1:
    if n % k == 0:
        n = n // k
        c += 1
    else:
        n -= 1
        c += 1

print(c)

#### 수학적 접근
result = 0

while True:
    target = (n//k)*k #k로 나눌수 있는 가장 가까운 수
    result += (n - target) # target으로 나누기전 1씩 빼야하는 한번에 적기
    n = target
    if n > k: # k가 n 보다 크면 나눌수 없기 때문에
        break
    result += 1
    n //= k

result += (n-1) # 못 나누는 것 1씩 빼기
print(result)