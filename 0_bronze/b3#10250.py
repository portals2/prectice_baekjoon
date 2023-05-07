# for문 2개로 10번째 사람 나오면 프린트

c = int(input())

for k in range(c):
    h, w, n = map(int, input().split(' '))
    for i in range(w):
        for j in range(h):
            n -= 1
            if n == 0:
                if i >= 9:
                    print(str(j+1)+str(i+1))
                else:
                    print(str(j+1)+'0'+str(i+1))
                    
## 모범답안
# tc = int(input())
# for _ in range(tc):
#     h, w, n = [int(x) for x in input().split()]
#     y = (n-1) % h + 1
#     x = (n-1) // h + 1
#     print("{0}{1:02}".format(y, x))