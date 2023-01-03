alpha = input()
alpha = alpha.upper()
alpha = list(alpha)

count={}
for i in alpha:
    try: count[i] += 1
    except: count[i]=1

result = set()
for i in count:
    if count[i] >= max(count.values()):
        result.add(i)

if len(result) >= 2:
    print('?')
else:
    print(max(count,key=count.get))

# print(list(count.values()).count(2))

#     밸류의 수 중에서 /세라 /밸류의 가장큰 수                     
# list(freq.values()).count(max(freq.values()))
# >>> 밸류의 가장 큰 수 x가 몇개가 있는지 카운트

# words = input().upper()
# unique_words = list(set(words))

# cnt_list = []
# for x in unique_words :
#     cnt = words.count(x) # aazzzz도 2, 4 zzzzaa도 2,4
#     cnt_list.append(cnt)

# if cnt_list.count(max(cnt_list)) > 1 :
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list))
#     print(unique_words)
#     print(cnt_list)
#     print(max_index)
#     print(unique_words[max_index])

# 용재 코드
# n = input()
# a = list(n.upper())
# l = set(a)

# maxNum = 0
# q = False
# g = ''

# for i in l:
#     c = a.count(i)
    
#     if c > maxNum:
#         g = i
#         maxNum = c

#     elif c == maxNum:
#         q = True


# if q == True:
#     print('?')

# else:
#     print(g)