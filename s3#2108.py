# import math
from collections import Counter
import sys
input=sys.stdin.readline

n = int(input()) #n은 홀수

num = []

for i in range(n):
    num.append(int(input()))

print(round(sum(num)/n))

s_num = sorted(num)
print(s_num[len(num)//2])


a = sorted(Counter(s_num).items(), key=lambda x: x[1], reverse=True)
if len(a) == 1:
    print(a[0][0])
elif a[0][1] == a[1][1]:
    print(a[1][0])
else:
    print(a[0][0])

print(max(num)-min(num))