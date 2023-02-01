# 1~n까지 차례로 push 하면서 수열 만들기
# from collections import deque
# import sys
# input=sys.stdin.readline

# n = int(input())


# stack = deque([0])
# c = []
# cc =[]
# k=1

# for i in range(n):
#     a = int(input())
#     for j in range(k, a+1):
#         if a == stack[-1]:
#             c.append(stack.pop())
#             cc.append('-')
#             break
#         elif (j not in stack) and (j not in c) :
#             stack.append(j)
#             cc.append('+')
#             k=j
       
# print(stack)
# print(c)
# print(cc)    

# if len(stack) != 1:
#     print('NO')
# else:
#     [print(i) for i in cc]


### 모범답안

n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())

    # 일정한 수 이하는 신경 쓰고 싶지 않은 경우
    # 아래와 같이 cur을 두어서 기준을 늘려서 제거할 수 있다.
    # for문도 작성은 가능하지만 if문 안에서 작동해야 함으로 
    # while문이 더 깔끔하게 작성 할 수 있다.
    while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur += 1 #만약 4다음 3이라면 이미 stack에 3이 있기 때문에
                 #더이상 stack에 숫자를 추가하지 않은다.
                 
    # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
        flag = 1            # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        break               

if flag == 0:
    for i in answer:
        print(i)
    