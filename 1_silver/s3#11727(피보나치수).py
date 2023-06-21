n = int(input())

a = [1,3] # 2번째 경우의 수가 2x2 박스가 추가되면서 증가했다.
c = 0
if n == 1:
    print(1)
else:
    for i in range(2, n):
        num = (a[i-1] + a[i-2]*2)
        a.append(num)
    print(a[-1]%10007)