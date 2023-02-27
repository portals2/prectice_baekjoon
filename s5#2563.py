# import sys
# input=sys.stdin.readline
# n = int(input())

# s= []
# s_a = n*100

# for i in range(n):
#     s.append(list(map(int,input().split())))

# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         if (abs(s[i][0] - s[j][0]) < 10) and (abs(s[i][1] - s[j][1]) < 10):
#             print(s[i], s[j])


#0번 부터 전체로 

# 3,7 / 13, 17
# 5,2 / 15, 12 >> 10이상 차이나면 ㄱㅊ
# 작은 숫자에 차이값을 더한다. x축 기준 2차이니까 3+2 = 5 ~ 13


# 모범 답안
# 이차원 배열을 통해서 겹친 부분을 제외하고 더한다.
n = int(input())
array = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화
for _ in range(n):  # 입력 받은 도화지 개수만큼 돈다.
    y1, x1 = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.

    for i in range(x1, x1 + 10):  # 세로를 돈다.
        for j in range(y1, y1 + 10):  # 가로를 돈다.
            array[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.

result = 0  # 넓이를 출력할 변수
for k in range(100):  # 전체 도화지를 돌면서
    result += array[k].count(1)  # 1 개수만 세어준다

print(result)