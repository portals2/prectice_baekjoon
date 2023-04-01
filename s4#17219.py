import sys
input=sys.stdin.readline

n, m = list(map(int, input().split(' ')))

www = {}
for i in range(n):
    w, p = input().split(' ')
    www[w] = p

for i in range(m):
    ww = input().rstrip()
    print(www[ww])