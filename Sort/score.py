N = int(input())

name_score = []
for i in range(N):
    name_score.append(input().split())
    
names = []
scores = []
for i in range(N):
    names.append(str(name_score[i][0]))
    scores.append(int(name_score[i][1]))

print(names, scores)

count_list = [[] for i in range(100)]

for i in range(N):
    count_list[scores[i] - 1].append(names[i])
    
for l in count_list:
    for name in l:
        print(name, end=" ")
    