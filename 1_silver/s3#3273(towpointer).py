# 투포인트와 정렬을 이용
# 오름차순 정렬후 x값을 찾으면 기록 후
# 왼쪽 포인트 이동
# 1 2 2 4 5 5 6 // 7 (1 6) (2 5) (2 5)
# end가 끝에 가면 다시 스타트로 이동

# 좌우로 오는 towpointer도 가능
n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

s = 0
e = n-1
c = 0


while s < e:
    # if e == len(a):
    #     e = s

    if a[s] + a[e] < x:
        s += 1
    elif a[s] + a[e] > x:
        e -= 1
    else:
        c += 1
        s += 1
        e -= 1
        
print(c)
