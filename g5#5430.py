'''
1324
4321
21
'''
n = int(input())

for i in range(n):
    s = list(input())
    num = int(input())
    arr = input()[1:-1].split(',')
    f = 1
    for i in s:
        if i == 'D':
            if arr == [''] or arr == []:
                f = 0
                break
            if f%2 == 1:
                arr.pop(0)
            else:
                arr.pop()
        else:
            f += 1
    if f%2 == 0:
        arr.reverse()
    if f != 0:
        print('[', end='')
        for i in arr[:-1]:
            print('{},'.format(i), end='')
        if arr != []:
            print('{}]'.format(arr[-1]))
        else:
            print(']')
    else:
        print('error')

'''
모든 reverse를 수행하지 않아야 한다.
즉 reverse를 대체할 수 있어야한다.
'''

# 질문게시판 5430번 - AC 
# https://www.acmicpc.net/board/view/115613
# 2023.04.23

# import sys
# from collections import deque
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     buffer = input().strip()
#     n = int(input())
#     l = input().strip()
#     l = l.replace('[', '')
#     l = l.replace(']', '')
#     if l != '':
#         l = list(map(int, l.split(',')))

#     queue = deque()
#     flag = 1
#     for idx in l:
#         queue.append(idx)
#     for i in range(len(buffer)):
#         if buffer[i] == 'R':
#             flag += 1
#         elif buffer[i] == 'D':
#             if len(queue) == 0:
#                 flag = 0
#                 break
#             else:
#                 if flag % 2 == 1: # reverse가 홀수면 정상
#                     queue.popleft()
#                 else: # reverse가 짝수면 뒤집힘
#                     queue.pop()

#     if flag == 0:
#         print('error')
#     else:
#         if flag % 2 == 0:
#             queue.reverse()
#         print("[", end='')
#         for i in range(len(queue)):
#             print(queue[i], end='')
#             if i != len(queue) - 1:
#                 print(',', end='')
#         print(']')