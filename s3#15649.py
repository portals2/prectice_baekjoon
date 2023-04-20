from itertools import permutations

a,b = map(int, input().split(' '))

for i in permutations(range(1, a+1), b):
    for j in i:
        print(j, end=' ')
    print()

