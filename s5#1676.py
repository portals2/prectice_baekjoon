import math
a = int(input())
n = list(str(math.factorial(a)))
n.reverse()

c = 0

for i in n:
    if i == "0":
        c+= 1
    else:
        break

print(c)
