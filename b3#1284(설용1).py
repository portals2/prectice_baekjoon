while True:
    a_ = 1
    a = list(input())
    if a[0] == '0':
        break
    for i in a:
        if a == '1':
            a_ += 2
        elif a == '0':
            a_ += 5
        else:
            a_ += 4
    print(a_)

   