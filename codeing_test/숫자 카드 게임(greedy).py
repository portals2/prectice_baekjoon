n, m = map(int, input().split())

# c = [[] for _ in range(n)]
c = []

for i in range(n):
    c.append(min(list(map(int, input().split()))))

print(max(c))
