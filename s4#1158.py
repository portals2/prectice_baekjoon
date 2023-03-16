import sys

N,K = map(int, sys.stdin.readline().split())
answer= []
arr= [i for i in range(1, N+1)]
j= 0

for _ in range(N):
    j+= K-1
    if j >= len(arr):
        j= j%(len(arr)) 
    answer.append(arr.pop(j))
    
answer= map(str, answer)
print('<{}>'.format(', '.join(answer)))
