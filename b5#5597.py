a = [False for i in range(30)]

for i in range(28):
    n = int(input())
    a[n-1] = True

for i in range(2):
    print((a.index(False))+1)
    a[a.index(False)] = True

# # 대조군으로 비교하는 법
# import sys

# a = [i for i in range(1, 31)]
# b = [int(sys.stdin.readline()) for i in range(28)]
# for i in a:
#     if i not in b:
#         print(i)