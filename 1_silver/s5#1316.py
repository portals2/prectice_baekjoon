n = int(input())

for i in range(n):
    a = []
    w = list(input())
    p_j = ""
    for j in w:
        if j not in a:
            a.append(j)
            p_j = j
        elif j==p_j:
            pass
        else:
            n -= 1
            break
print(n)

# # 짧은 답안
# n = int(input())

# for i in range(n):
#     word = input()
#     a = list(word)

# key=word.find는 중복인 문자를 한쪽으로 뭉쳐준다.
#     if a != sorted(a, key=word.find):  
#         n -= 1

# print(n)