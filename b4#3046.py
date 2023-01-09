# (R1+R2)/2 = S
# S *2 -r1 =r2

r1, s = map(int, input().split(' '))
if (-1000 < r1 < 1000) and  (-1000 < s < 1000):
    print(s*2-r1)