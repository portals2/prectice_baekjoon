import sys

N,K = map(int, sys.stdin.readline().split())
answer= []
arr= [i for i in range(1, N+1)]
j= 0

for _ in range(N):
    j+= K-1 #j=0으로 시작하고 for문 앞에서 +=시켜주는 경우 맞음
    if j >= len(arr):
        j= j%(len(arr)) 
    answer.append(arr.pop(j))
    
answer= map(str, answer)
print('<{}>'.format(', '.join(answer)))
