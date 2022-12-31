how_num = int(input())

ans = list(str(input()) for i in range(how_num)) 

for i in range(how_num):
    k = 0
    count = 0
    for j in range(len(ans[i])):
        if ans[i][j] == 'O':
            k += 1
            count += k
        else:
            k = 0
    print(count)

# N=int(input())
# for i in range(N):
#     a=input()
#     n=0
#     ad=0
#     for j in a:
#         if j=='O':
#             n=n+1
#         else:
#             n=0
#         ad=ad+n
#     print(ad)