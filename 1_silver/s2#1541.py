# c = input()

# fleg = 0
# prev_idx = 0
# result = 0

# for i in range(len(c)):
#     if (c[i] == '+' or c[i] == '-') and fleg == 0:
#         result += int(c[prev_idx : i])
#         prev_idx = i+1
#         if c[i] == '-':
#             fleg = 1
#     elif c[i] == '-' or c[i] == '+':
#         fleg = 1
#         result -= int(c[prev_idx : i])
#         prev_idx = i+1


# if fleg == 0:
#     result += int(c[prev_idx:])
# else:
#     result -= int(c[prev_idx:])
# print(result)

#### 모범답안
# 10+20+30+40
# 55-50+40
import sys

board = sys.stdin.readline().split("-") 
# -로 spilt하여서 만약 떨어진다면
# 그 덩어리는 모두 음수처리한다.
print(board)

res = 0
for i in board[0].split("+"):
    res += int(i)
for i in board[1:]:
    for j in i.split("+"): #모두 음수 처리 하는 부분
        res -=int(j)
print(res)