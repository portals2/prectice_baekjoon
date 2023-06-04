for i in range(3):
    l = list(map(int, input().split(' ')))
    if l[2] > l[5]:
        if l[1] < l[4]:
            h = l[3] - l[0] 
            m = l[4] - l[1] -1
            s = l[5] - l[2] +60
        else:
            h = l[3] - l[0] -1
            m = l[4] - l[1] +59
            s = l[5] - l[2] +60
    elif l[1] > l[4]:
        h = l[3] - l[0] -1
        m = l[4] - l[1] +60
        s = l[5] - l[2]
    else:
        h = l[3] - l[0]
        m = l[4] - l[1]
        s = l[5] - l[2]
    print(h, m, s)


