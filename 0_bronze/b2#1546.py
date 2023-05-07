how_num = int(input())
num = map(float, input().split(' '))

a = list(num)[:how_num]
big_a = max(a)
for i in range(len(a)):
    a[i] = a[i]/big_a*100

print(sum(a)/how_num)