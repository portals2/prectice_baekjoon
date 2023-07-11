# # 시간 초과 난다는데?
# import sys
# input = sys.stdin.readline().rstrip

# s = list(input())

# a = []

# for i in range(1, len(s)+1):
#     for j in range(len(list(s))):
#         if s[j:j+i] not in a:           
#             a.append(s[j:j+i])
#         if j+i == len(s)+1:
#             break

# print(len(a))

#### 
import sys
# input = sys.stdin.readline

text = input()
_set = set()

for i in range(len(text)):
    for j in range(i, len(text)):
        _set.add(text[i:j+1])
        
print(len(_set))
