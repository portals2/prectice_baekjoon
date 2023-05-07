import math
t = int(input())    

for i in range(t):
    n,m = map(int, input().split())
    a= math.factorial(n)
    b= math.factorial(m-n)
    c= math.factorial(m)
    print(c//(a*b))



