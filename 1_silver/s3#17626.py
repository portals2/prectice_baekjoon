# n = int(input())

# l = [ i**2 for i in range(1, int((n**(1/2))+1))]

# l = sorted(l, reverse=True)

# c = 0

# for i in l:
#     if n <= 81:
#         c+=1
#         print(c)
#         break
#     elif n > i:
#         n -= i
#         c += 1

#### dfs 
# import sys
# N = int(sys.stdin.readline().strip())
# squares = [n**2 for n in range(int(N**(1/2))+1)]
# total = 0
# nums = [N]
# while len(nums) > 0:
#     total += 1
#     temp = set()
#     for num in nums:
#         for n in squares:
#             if n <= num:
#                 temp.add(num-n)
#     #print(temp)
#     if 0 in temp:
#         break
#     nums = list(temp)
# print(total)

#### dp
N = int(input())
dp = [0,1]
for i in range(2, N+1):
    min_value = 1000000
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1

    dp.append(min_value + 1)
print(dp)
print(dp[N])

#11339