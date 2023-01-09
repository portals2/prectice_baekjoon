#어떻게 M에 가장 가까운 3장을 뽑을까?
# 가까운수 >> 뺴서 차이가 가장 안나는 수
# 3장 뽑기는?? 단수 비교후 리스트 저장
# 느리지만 가장 확실

n, m = map(int, input().split(' '))

num = list(map(int, input().split(' ')))
a = []
b = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if m -(num[i]+num[j]+num[k]) >= 0:
                b.append(num[i]+num[j]+num[k])
                

print(max(b))


