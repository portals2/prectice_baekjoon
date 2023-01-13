# 알고리즘
# import sys

# n = int(input())

# a=[]
# for i in range(n):
#     a.append(int(sys.stdin.readline()))

# def mergesort(list):
#     left = []
#     right = []
#     if len(list) <= 1:
#         return(list)
#     else:
#         middle = len(list)//2
#         for i in list[:middle]:
#             left.append(i)
#         for i in list[middle:]:
#             right.append(i)
#         left = mergesort(left)
#         right = mergesort(right)
#         return merge(left, right)

# def merge(left, right):
#     result=[]
#     while (len(left)>0) and (len(right)>0):
#         if left[0]<= right[0]:
#             result.append(left[0])
#             del left[0]
#         else:
#             result.append(right[0])
#             del right[0]
#     if len(left) > 0:
#         for i in range(len(left)):
#             result.append(left[i])
#     if len(right) > 0:
#         for i in range(len(right)):
#             result.append(right[i])

#     return result
           
# for i in mergesort(a):
#     print(i)

################ 딕셔너리
import sys
n = int(input())

count={}
for i in range(n):
    a = int(sys.stdin.readline())
    if a not in count:
        count[int(a)]=1
    else:
        count[a] += 1

for i in sorted(count):
    for j in range(count[i]):
        print(i)

#### 리스트
# import sys
# n=int(input())
# num=[0]*10001
# for _ in range(n):
#     num[int(sys.stdin.readline())]+=1
# for i in range(1, 10001):
#     while num[i]>0:
#         print(i)
#         num[i]-=1