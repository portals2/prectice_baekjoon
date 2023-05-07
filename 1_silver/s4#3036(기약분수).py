import fractions
n = int(input())

a = list(map(int, input().split(' ')))

for i in range(1,n):
    c = fractions.Fraction(a[0], a[i])
    print('{}/{}'.format(c.numerator, c.denominator))


####모범답안
# gcd는 무슨 방법으로 구하는 것일까
# 기약분수...
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():

    N = int(input())
    radius = list( map( int, input().split() ) )

    first = radius[0] # 첫 번째 링의 반지름

    for items in radius[1:]:
        radius_gcd = gcd(first, items) # 첫 번째 링과 각 링의 비율을 기약분수로 변환
        numerator = first // radius_gcd
        denominator = items // radius_gcd
        print(f"{numerator}/{denominator}") # 기약분수 형태로 출력

if __name__ == "__main__":
    main()