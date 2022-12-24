# How are you today?
# Quite well, thank you, how about yourself?
# I live at number twenty four.
# #

# 7
# 14
# 9

#for로 [] 인덱싱에 모음 추출
# a = "How are you today?"
# print(a[1])
# ((1),(2),(3))
# [[0,0],[1,0],[2,0]]


sentens = []
n = ''
while n != '#':
    n = input().lower()
    sentens.append(n)
# print(sentens)

for i in range(len(sentens[0:-1])):
    # print(sentens[i])
    count = 0
    for j in range(len(sentens[i])):
        # print(j)
        if ((sentens[i][j] == 'a') or (sentens[i][j] == 'e') 
        or (sentens[i][j] == 'i') or (sentens[i][j] == 'o') 
        or (sentens[i][j] == 'u')):
            count += 1
    print(count)


