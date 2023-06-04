x = 0 # 총합
y = 0 # 학점*평점
for i in range(20):
    a,b,c = map(str, input().split(' '))
    if c == 'P':
        pass
    else:
        x += float(b)
        if c == 'A+':
            y += float(b)*4.5
        elif c == 'A0':
            y += float(b)*4.0
        elif c == 'B+':
            y += float(b)*3.5
        elif c == 'B0':
            y += float(b)*3.0
        elif c == 'C+':
            y += float(b)*2.5
        elif c == 'C0':
            y += float(b)*2.0
        elif c == 'D+':
            y += float(b)*1.5
        elif c == 'D0':
            y += float(b)*1.0
        elif c == 'F':
            y += float(b)*0.0

print(y/x)
        