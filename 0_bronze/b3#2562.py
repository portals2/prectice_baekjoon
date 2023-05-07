pre_num = 0
nan_ban = 0
for i in range(9):
    num = int(input())
    if num > pre_num:
        pre_num = num
        nan_ban = i + 1

print(pre_num)
print(nan_ban)
