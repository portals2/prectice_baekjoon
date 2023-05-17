a = input()

if len(a) < 3:
    print(int(a[0]) + int(a[1]))
else:
    print(int(a[:2]) + int(a[2:]))