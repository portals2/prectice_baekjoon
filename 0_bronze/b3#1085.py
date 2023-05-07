# x,y 가 0이 되는 최솟값이나 w, h가 되는 최솟값

x,y,w,h = map(int, input().split(' '))

result = []
for i in ((w-x), (h-y),x, y):
    result.append(i)
print(min(result))

# 리스트에서 바로 연산이 가능하다.
# x, y, w, h = map(int, input().split())
# dist = [x, y, w-x, h-y]
# print(min(dist))
# print(min(w-x, x, h-y, y))
