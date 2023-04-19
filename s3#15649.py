# from itertools import permutations

# a,b = map(int, input().split(' '))

# for i in permutations(range(1, a+1), b):
#     for j in i:
#         print(j, end=' ')
#     print()

def solve(m:int, bt:list):
    if m == 1:
        for i in range(1, n+1):
            if str(i) not in bt:
                print(' '.join(bt), i)
    
    for i in range(1, n+1):
        if str(i) not in bt:
            solve(m-1, bt+[str(i)])

n, m = map(int, input().split())

solve(m, list([]))