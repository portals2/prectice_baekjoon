n = int(input())
i = 666
#str일 경우 부분 포함을 구분할 수 있다.
while n != 0:
    if '666' in str(i):
        n -= 1
    if n == 0:
        print(i)
    i += 1