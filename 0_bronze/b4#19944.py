a,b = map(int, input().split(' '))  

if b == 1 or b == 2:
    print('NEWBIE!')
elif a >= b and 2 < b:
    print('OLDBIE!')
else:
    print('TLE!')