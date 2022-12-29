rest = [i%42 for i in [int(input()) for j in range(10)]]
rest = set(rest)
rest = list(rest)
print(len(rest))

# a=set()
# for i in map(int,open(0).read().split()):a.add(i%42)
# print(len(a))