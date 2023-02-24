def sosu(N):
    # check=1
    if N==1:
        return 0
    for j in range(2, int(N**(1/2))+1):
        if N%j==0:
            # check=0
            return 0
    else:
        return 1

s = []
a = int(input()) 
b = int(input())
for i in range(a,b+1):
    if sosu(i)==1:
        s.append(i)

if len(s) >= 1:
    print(sum(s))
    print(min(s))
else:
    print(-1)