while True:
    a= input()
    if a == 'END':
        break
    else:
        r_a = ''
        for i in a:
            r_a = i + r_a

        aa = r_a.split(' ')
        for i in range(0, len(aa)):
            print(aa[i], end=' ')
        print('')

#### 모범답안
while True:
    word = input()
    if word == "END":
        break
    else:
        word = word[::-1]
        print(word)