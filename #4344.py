how_num = int(input())
score = []


for i in range(how_num):
    score.append(list(map(float, input().split(' '))))
    
for i in range(how_num):
    count = 0
    num = sum(score[i][1:]) / score[i][0]
    for j in score[i][1:]:
        if num < j:
            count += 1
    print("{0:.3f}%".format(count / score[i][0] * 100))

