# # (1,1)2 (1,2)3 (1,3)4
# # (2,2)4 6
# # 8
# # a1

# a = list(str(input()))

# x = 0
# y = int(a[1]) # 8 7도 x처럼 1과 2로 변환 했어야 했다.

# # if a[0] == 'a' or a[0] == 'h':
# #     x = 1
# # elif a[0] == 'b' or a[0] == 'g':
# #     x = 2
# # else:
# #     x = 3

# if a[0] == 'a' or a[0] == 'h':
#     x = 1
# elif a[0] == 'b' or a[0] == 'g':
#     x = 2
# else:
#     x = 3

# if y == 8: ## 수정된 부분
#     y = 1
# elif y == 7:
#     y =2

# if x == 1 and y == 1:
#     print(2)
# elif (x == 2 and y == 1) or (x == 1 and y == 2):
#     print(3)
# elif (x == 3 and y == 1) or (x == 1 and y == 3):
#     print(4)
# elif (x == 2 and y == 2) or (x == 2 and y == 2):
#     print(4)
# elif (x == 2 and y == 3) or (x == 3 and y == 2):
#     print(6)
# else:
#     print(8)


####모범답안

a = input()
row = int(a[1])
column = int(ord(a[0])-ord('a')) + 1

move_able = [(-2,-1),(-1,-2),(1,-2),(-1,2),(2,1),(1,2),(2,-1),(-2,1)]

result = 0

for move in move_able:
    moved_row = row - move[1]
    moved_column = column - move[0]
    if (0 < moved_row < 9) and (0 < moved_column< 9):
        result += 1

print(result)