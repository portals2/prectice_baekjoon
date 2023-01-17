t = int(input())

for i in range(t):
    l = 0
    ps = list(map(str, input()))
    for j in ps:
        if l < 0:
            break
        if j == '(':
            l += 1
        elif j == ')':
            l -= 1
    if l == 0:
        print('YES')
    else:
        print('NO')     

## 안에 값이 존재하는 지에 따라서 if문으로 구분할 수 있다.
# stack = []

# if stack:
#     print('Ture')
# else:
#     print('False')
        
