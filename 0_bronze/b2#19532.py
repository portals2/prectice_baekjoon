a,b,c,d,e,f = map(int, input().split(' '))

# q = (b*d)-(e*a)
# w = (c*d)-(f*a)
# y = (w//q)

# qq =(b*y) 
# x = ((c - qq)//a)
# print(x, y)

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if ((a*i)+(b*j) == c) and ((d*i)+(e*j) ==f):
            print(i, j)


#수학적으로 접근
a, b, c, d, e, f = map(int, input().split())

# 연립 방정식 해 구하기
x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print(x, y)