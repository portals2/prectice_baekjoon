how_num = int(input())
num = map(int, input().split(' '))

a = list(num)[:how_num]
print(min(a), max(a))  