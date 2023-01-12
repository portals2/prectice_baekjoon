# 간단하게는 수열의 값을 모두 더할 수도 있다. 
# 해시 함수의 정의에서 유한한 범위의 출력을 
# 가져야 한다고 했으니까 적당히 큰 수 M으로 
# 나눠주자.

n = int(input())
s = list(str(input()))

count={}
for i in range(97, 123):
    try: count[chr(i)]= (i-96)
    except: pass

a=[]
for i in range(n):
    a.append(int(count[s[i]])*(31**i))
print(sum(a)%1234567891)