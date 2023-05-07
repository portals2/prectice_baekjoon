n = int(input())

s = 0

for i in range(1,n+1):
    print(" "*s, end='')
    print('*'*((2*n+1-1)-(2*i-1)))
    s += 1

# #모범 답안
# n=int(input())
# for i in range(n,0,-1): #세번째에 -1을 사용 하면 1씩 줄어든다.
#     print(' '*(n-i)+'*'*(2*i-1))