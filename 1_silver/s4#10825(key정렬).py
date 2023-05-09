# >>> tuple_list = [('좋은하루', 0),
#     	          ('niceday', 1), 
#     	          ('좋은하루', 5), 
#     	          ('good_morning', 3), 
#     	          ('niceday',5)]
                  
# >>> tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능
# >>> print(tuple_list)
# [('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]


import sys
input=sys.stdin.readline
n = int(input())

a = []

for i in range(n):
    a.append((input().split(' ')))

a.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
                                  # 처음에 int를 넣지 않고는 틀렸는데
                                #   왜 int룰 넣으니까 정답이지??

for i in a:
    print(i[0])


