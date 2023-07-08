# <ab cd>ef gh<ij kl>
a = input()
a_ = a.replace('<', ' ').replace('>', ' ').split(' ')
a_r = list(a)
q = []

s = 0
e = 0
i = 0

while i < len(a_):
    if a_[i] == '':
        if a_r[i] == '<' or a_r[i] == '>':
            q.append(a_r[i])
        q.append(i)
    i += 1
    
    
    
print(q)

# #### 모범답안
# stmt=list(input())
# # 숫자와 문자열만 뒤집고, 나머지는 그대로 유지한다.
# Stack=[]
# Result=[]
# Special=False
# for i in stmt:

#     # < 와 >사이에는 특수상태 유지를 위해서 boolean타입인 Special을 추가하여, 역순출력을 방지한다.
#     # 즉, <를 만나면 Special이 True가 되어서 >를 만나기 전까지 하위 False는 절대로 실행이 되지 않는다.
#     if i=="<":
#         # 앞에 Stack에 누적된 값들을 싹다 비워준다.
#         while Stack:
#                 Result.append(Stack.pop())
#         Special=True
#     # Special이 True인 경우는 바로 Result에 추가를 한다.
#     if Special:
#         Result.append(i)
#     if i==">":
#         Special=False
#         continue

#     if Special==False:
#         if i.isalnum():
#             Stack.append(i)
#         else:
#             # 알파벳이 아닌 경우,
#             # Stack 내부에 저장된 것을 순차적으로 Result에 옮겨 담는다 + i를 추가한다.
#             while Stack:
#                 Result.append(Stack.pop())
#             Result.append(i)


# while Stack:
#     Result.append(Stack.pop())
# for i in Result:
#     print(i,end="")
