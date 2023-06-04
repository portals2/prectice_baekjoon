a = int(input())
b = int(input())
c = int(input())
s = a+b+c
if a == b == c == 60:
    print('Equilateral')
elif s == 180:
    if a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')