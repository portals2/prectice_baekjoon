# from collections import deque
# # 더블 링크드 리스트를 사용한다.

# queue = deque()
# answer = []

# n, k = map(int, input().split())

# # 1~n번째의 리스트를 만드는 작업
# for i in range(1, n+1):
#     queue.append(i)

# while queue:
#     # k=3일 경우 0과 1번째의 수를 두로 보내는 방식으로 index[3]의
#     # 숫자를 answer칸에 pop했다.
#     for i in range(k-1):
#         queue.append(queue.popleft())
#     answer.append(queue.popleft())

# print("<",end='')
# for i in range(len(answer)-1):
#     print("%d, "%answer[i], end='')
# print(answer[-1], end='')
# print(">")

import sys

n, k = map(int, sys.stdin.readline().split())

queue = [i for i in range(1, n + 1)] #(1~n)
temp = [] # 정답칸
index = 0 # 제거할 인덱스

while queue:
    index += k - 1 
    # 인덱스 는 1이 부족하니까 3의 배수에서 6의 인덱스는 3*2 = 6에서
    # 1을 뺴는 것으로 구할 수 있다.
    # 반대로 인덱스에서 수를 구하는 것은 (k-1)n+1을 하는 것으로 
    # 구할 수 있다. 

    # 현재의 문제의 경우 pop을 이용해서 리스트에서 숫자를 제게해야
    # 함으로 +1을 제거한 k-1만을 사용한다. 시밧비사비사비사비사비

    if index >= len(queue):
        index %= len(queue)
    # 나머지는 연결 되었을 때 이어지는 값으로 123 1 같은 경우이다.

    temp.append(str(queue.pop(index)))
    

# sep 함수를 통해 소괄호 공간을 없앤다.
print("<", ", ".join(temp), ">", sep="")