import sys
input=sys.stdin.readline
n = int(input())

arr = []
c = 2
s = 2
i = 2
j = 3


if n == 1:
    print('1/1')   
else:
    while True:
        if (n >= i) and (n <= j):
            if c%2 != 0:
                for k in range(1, (n-i)+2):
                    arr.append(f'{c}/{k}')
                    c -= 1
            else:
                for k in range(1, (n-i)+2):
                    arr.append(f'{k}/{c}')
                    
                    c -= 1
            break
        else:
            i = j+1
            s += 1
            j = j+s
            c += 1
       
    print(arr[-1])

#짝수는 False 홀수는 True