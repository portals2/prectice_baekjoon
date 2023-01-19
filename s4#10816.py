n = int(input())
num = list(map(int, input().split(' ')))
count = {}
for i in num:
    
    if i not in count:
        count[i]=1
    else:
        count[i] += 1

# print(count)

m = int(input())
num = map(int, input().split(' '))

a = []

for i in num:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')
# 백준에서는 정답에 마지막이 공백이여도 상관없음