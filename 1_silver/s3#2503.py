n = int(input())
arr = [True] * 1000 #일단 모든 경우를 True로 합니다.
#각 자리가 서로 다른 숫자여야 하는데 같은 숫자거나 0이 포함된 수는 False로 설정합니다.
for i in range(123, 1000):
    l = str(i)
    if l[0]==l[1] or l[1]==l[2] or l[0]==l[2]:
        arr[i] = False
    if '0' in l:
        arr[i] = False
for i in range(0, n):
    tmp_arr = input().split()
    number = int(tmp_arr[0])
    strike = int(tmp_arr[1])
    ball = int(tmp_arr[2])
    for j in range(123, 1000):
        #세자리 수들을 입력받은 수랑 비교하여 스트라이크 개수와 볼 개수를 셉니다.
        # 즉 모든 경우에 수중 입력받은 정보들과 같은 수만 비교한다.
        strike_cnt = 0
        ball_cnt = 0
        for x in range(0, 3):
            for y in range(0, 3):
                if x==y and str(number)[x]==str(j)[y]: # 숫자의 위치와 크기가 같은 경우
                    strike_cnt = strike_cnt + 1
                elif str(number)[x]==str(j)[y]: # 숫자 위치는 같지 않지만 같은 숫자가 있을 경우
                    ball_cnt = ball_cnt +1
        #구한 스트라이크 개수와 볼 개수가 입력받은 개수들이랑 다를경우 False로 처리합니다.
        if strike!=strike_cnt or ball != ball_cnt:
            arr[j] = False

#세자리 수 중에서 True인 개수를 출력합니다.
print(arr[123:1000].count(True))