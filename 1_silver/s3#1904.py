# #재귀로 풀기에는 너무 오래 걸린다.
# import sys
# sys.setrecursionlimit(10**9) # 재귀 설정
# input = sys.stdin.readline

# n = int(input())

# t = [1,2] # 1의 타일 1개, 00의 타일 2개

# count = 0
# cc = 0

# def btk(start):
#     global count
#     global cc

#     if count > n: 
#         return
#     elif count == n:
#         cc += 1
#         return

#     for i in t:
#         count += i
#         btk(i)
#         count -= i

# btk(1)
# print(cc % 15746)

####
a = [0]*1000001 #동적 계획이므로
a[1]=1
a[2]=2

for i in range(3,1000001):
    a[i]=a[i-1]+a[i-2] #피보나치 수열로 푸는것이므로
    if a[i]>=15746: 
        a[i]=a[i]%15746 #15746보다 커지면 계산 시간 늘어나므로 미리 나머지 계산

        
b=int(input())
print(a[b]) # 15746 보다 큰 숫자는 이미 위에서 제거 했으므로