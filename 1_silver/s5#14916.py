n = int(input())
count = 0

if n % 5 == 0:
    print(n // 5)
else:
    while True:
        n -= 2
        count += 1
        if n < 0:
            print("-1")
            break
        elif (n % 5) == 0:
            count += n // 5
            print(count)
            break
