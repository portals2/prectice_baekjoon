def make_sequence(n, sequence):
    stack = []
    result = []
    current = 1
    for x in sequence:
        while current <= x:
            stack.append(current)
            current += 1
            result.append("+")
        if stack[-1] == x:
            stack.pop()
            result.append("-")
        else:
            return "NO"
    return "\n".join(result)

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
print(make_sequence(n, s))