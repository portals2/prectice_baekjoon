a = input()

if len(a) < 3:
    print(int(a[0]) + int(a[1]))
else:
    if int(a[:2]) >10:
        print(int(a[:1]) + int(a[1:]))
    else:

        print(int(a[:2]) + int(a[2:]))