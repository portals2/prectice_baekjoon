# 100 > 100+1+0+0 = 101

# a의 범위를 10000으로 정하면 인덱스 에러가 나서
# 충분히 늘려주었다.
a = [False for i in range(11000)]

for i in range(1, 10001):
    a[i+sum(map(int, str(i)))] = True
    if a[i] == False:
        print(i)

