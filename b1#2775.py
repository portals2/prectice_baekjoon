# a층의 b호에 살려면 자신의 아래(a-1)층의 
# 1호부터 b호까지 사람들의 수의 합만큼 
# 사람들을 데려와 살아야 한다
# 1 2 3 4 5 6  >> 0층
# 1 3 6 10 15 21 >> 1층
# 1 4 10 20 ...

t = int(input())

for i in range(t):
    f = int(input())
    h = int(input())
    p = []
    k = []  
    for i in range(h):
        p.append(i+1)
        k.append(i)
    if f == 0:
        print(h)
    else:
        for i in range(f): #1
            for j in range(h): #2  
                k[j] = sum(p[:j+1])        
            p = k.copy()
        print(p[h-1])
