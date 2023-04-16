# n, m = map(int, input().split(' '))
# list1 = []
# for i in range(n):
#     list1.append(list(map(int, input().split(' '))))


# m_, k = map(int, input().split(' '))
# list2 = []
# for i in range(m_):
#     list2.append(list(map(int, input().split(' '))))

# print(list1,list2)
# # an = []
# # for i in range(n):
# #     l = []
# #     for j in a[i]:
# #         for v in range(m_):
# #             l += j * b[v]
# #     an.append(l)
# # print(an)

# # product = [x*y for x,y in zip(list1,list2)]
# print(list(zip(list1,list2)))


#### 모법답안
N, M=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(N)]

M, K=map(int, input().split())
b=[list(map(int, input().split())) for _ in range(M)]

asdf=[[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for l in range(M):
            asdf[i][j]+=a[i][l]*b[l][j]
            # a(3,2) b(2,3)일 때 a와b의 i,j가 바뀌면서 l이 한번씩
            # 모든 요소를 돌아가기 때문에
for r in asdf:
    for n in r:
        print(n, end=' ')
    print()