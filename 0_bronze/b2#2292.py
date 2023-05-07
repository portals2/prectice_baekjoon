#육각형을 중심으로 dept이 늘어날 때 마다 n이 몇씩 증가할까?
# 6개 씩 늘어남

n = int(input())

k = 1
for i in range(1, n+1):
    if n <= k:
        print(i)
        break
    k += 6*i
    # print(k)
# 1 6 12 18 24 30 36
#   7 19 37 61

