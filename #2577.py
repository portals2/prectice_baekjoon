# print(*map(input().find,map(str,range(10))))

a = int(input())
b = int(input())
c = int(input())

sum = a*b*c
count={}
for i in range(10):
    try: count[str(i)]= 0
    except: pass

for j in list(str(sum)):
    count[j] += 1

[print(a)for a in list(count.values())]

# 카운팅을 할 때 딕셔너리와 리스트의 속도 차이

# int 하나씩 나누기
# a=int(input())
# b=int(input())
# c=int(input())
# d=list(map(int,str(a*b*c)))
# print(d) # [1, 8, 6, 0, 8, 6, 7]

