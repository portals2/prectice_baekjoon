n = int(input())

a = '10'
c = 0

if n < 10:
    c = n

while n >= 10:
    if n >= int(a):
        c = c + (int(a)-(int(a)//10))*(len(a)-1)
        a += '0'
    else:
        c = c + (n - ((int(a)//10)-1))*(len(a)-1)
        break

print(c)

# 1-9 9 9*1
# 10-99 180 90*2 > 189 / 192
# 100-999 2700 900*3 


# 120 - 100 20*3 


# 1 10 100 1000
# 1  2   3    4

#### 내 답안을 간단히 하면
n = input()
length = len(n) - 1
result = 0
for i in range(length):
    result += (9 * (10 ** i)) * (i + 1) # i+1번째 자릿수의 숫자 개수 * 길이
result += ((int(n) - (10 ** length)) + 1) * (length + 1) # 가장 높은 자릿수의 숫자 개수 * 길이
print(result)
