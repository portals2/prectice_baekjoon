# a.sort(key= lambda x : (x[0]))

#x로 정렬하고 이후에 y로 정렬
import sys
input=sys.stdin.readline
n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split(' '))
    a.append((y,x))

# a.sort(key= lambda x : (x[0], x[1]))
# 원래 2차원 리스트에서 sort함수를 쓰면 
# 기본값으로 y값까지 알아서 정렬해줍니다.
a.sort()

for x, y in a:
    print(y,x)

