#한번에 입력을 받아야 한다.
#예시 입력을 자세히 확인하자
money, sel = input().split()
money = int(money)
sel = int(sel)

if (money >= sel and sel > 0 and money > 0):
    print(money // sel)
    print(money % sel)
else:
    pass