a,b = map(int, input().split())


# 유클리드 호제법
def gcd(m,n): 
    while n != 0: # n=0이면 m을 출력하고 종료
       t = m%n # m이 n으로 나누어 떨어지면 n을 출력
       (m,n) = (n,t) # 나머지가 있다면, m,n을 대입해 다시 계산
    return abs(m) 
  
gcd_ =gcd(a,b)

print((a*b)//gcd_)