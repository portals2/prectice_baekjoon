# 알파벳의 나열에서 단어에 알파벳이 있으면 
#처음 등장 위치를 아니면 -1을

st = input()
st = list(st)

count={}
for i in range(97, 123):
    for k in chr(i):
        try: count[k]= -1
        except: pass

for j in st:
    if count[j] == -1:
        count[j] += (st.index(j))+1

[print(s, end=' ')for s in list(count.values())]

# 백준 모범 답안
# print(*map(input().find,map(chr,range(97,123))))