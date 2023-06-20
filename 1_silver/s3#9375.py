from itertools import combinations

n = int(input())

for i in range(n):
    a = int(input())
    items = {}
    for j in range(a):
        item = list(map(str, input().split()))
        if item[1] not in items:
            items[item[1]] = 2 # 왜 2을 더하는 거지
        else:
            items[item[1]] += 1

    combinations = 1
    for value in items.values():
        combinations *= value
    print(combinations - 1)  


    # print(items)

####모범답안
# 230619

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    types = {}

    for _ in range(int(input())):
        cloth_name, cloth_type = input().split()
        if cloth_type in types.keys():
            types[cloth_type].append(cloth_name)
        else:
            types[cloth_type] = [cloth_name]
    # print(types)

    answer = 1
    for key in types.keys():
        answer *= len(types[key]) + 1
    answer -= 1 # 모두 안 입는 경우

    print(answer)