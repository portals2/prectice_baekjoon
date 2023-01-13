################ 시간 초과
# import sys
# n = int(sys.stdin.readline())

# count={}
# for i in range(n):
#     a = sys.stdin.readline().split()
#     if a[0] not in count:
#         count[a[0]]=len(a[0])

# count = sorted(count)
# for i in range(len(count)):
#     for j in range(len(count)):
#         if len(count[j]) == i+1:
#             print(count[j])
################# 모범 담안
import sys
n = int(sys.stdin.readline())
a = [sys.stdin.readline().strip() for i in range(n)]

a= list(set(a))
a.sort()
a.sort(key = len)

for i in a:
    print(i)

################ 모범 답안 2
# n = int(input())

# word = []
# for i in range(n):
#     word.append(input())
# set_word = list(set(word))

# sorted_word = []
# for i in set_word:
#     sorted_word.append((len(i), i))

# result = sorted(sorted_word)

# for len_word, word in result:
#     print(word)

