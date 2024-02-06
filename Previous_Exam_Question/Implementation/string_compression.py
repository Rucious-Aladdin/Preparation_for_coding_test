import copy

strings = input()
length_arr = [len(strings)] * (len(strings) // 2 - 1)

answers = []
temp = ""
for i in range(len(strings) // 2):
    temp = copy.deepcopy(strings)
    x =[]
    last = 0
    for j in range(i+1, len(temp),i + 1):
        x.append([1, temp[last:j]])
        last = j
    if last <= len(temp) - 1:
        x.append([1, temp[last:]])
    
    start = x.pop(0)
    y = [start]
    for cmp in x:
        if cmp[1] == y[-1][1]:
            y[-1][0] += 1
        else:
            y.append(cmp)
    if y[0][0] > 10:
        print(y)
    sum = 0
    for last_info in y:
        if last_info[0] == 1:
            sum += len(last_info[1])
        else:
            sum += (len(last_info[1]) + 1)
    answers.append(sum)

print(min(answers))
    