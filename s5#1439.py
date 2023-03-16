# s = input()
# z = 0
# o = 0

# if s[-1] == '0' and len(set(s)) == 2:
#     s += '1'
# else:
#     s += '0'

# for i in range(1, len(s)):
#     if s[i] == '0':
#         if s[i-1] == '1':
#             o += 1
#     if s[i] == '1':
#         if s[i-1] == '0':
#             z += 1


# print(min(z, o))

# 모범답안
# s = input()
# print(s.split('1'))
# print(s.split('0'))
# t = len([x for x in s.split('1') if x])
# u = len([x for x in s.split('0') if x])
# print((t, u))