l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

a_ = a/c
b_ = b/d

if a//c < a/c:
    a_ = a//c+1
if b//d < b/d:
    b_ = b//d+1

if int(l-max(a_,b_)) > 0:
    print(int(l-max(a_,b_)))
else:
    print(0)

#### 모범답안
L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())

langdays=A//C
if A%C>0: # 딱 떨어지지 않고, 4.1일 이 된다면 5일로 처리하는 법
    langdays+=1
mathdays=B//D
if B%D>0:
    mathdays+=1

print(L-max(langdays,mathdays))