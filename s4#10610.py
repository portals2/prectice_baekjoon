# n에는 0이 포함되어있어야 한다.
# 역순으로 정렬
# 1의 자리가 0

from itertools import permutations
n = list(map(str, (input())))
n = list(reversed(sorted(n)))

perm = permutations(n, len(n))
#7P4
c = 0
for p in perm:
	p = ''.join(p)
	if (p[-1] == '0') and (int(p) % 30 == 0):
		print(p)
		c = 1
		break
	elif c == 0:
		print(-1)
		break

# # 다른 방법
# # 30의 배수는 모든 자리의 수의 합 % 3 이 0이다.
# print(8+0+8+7+5+5+4+2) # 39%3 =0 0
# T = list(input())
# T.sort()

# hap = 0
# for i in T:
#     hap += int(i)

# T.reverse()
# if int(''.join(T)) % 30:
#     print(-1)
# else:
#     print(''.join(T))