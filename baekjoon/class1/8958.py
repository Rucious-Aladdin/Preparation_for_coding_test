N = int(input())
probs = []
for _ in range(N):
    l = list(input())
    l.append("X")
    probs.append(l)

for checks in probs:
    answer_sheet = []
    count = 0    
    while len(checks) != 0:
        if (checks[0] == "O"):
            old = checks.pop(0)
            count += 1
        else:
            if old == "O":
                answer_sheet.append(count)
                count = 0
                old ="X"
            checks.pop(0)
    sum = 0
    for x in answer_sheet:
        sum += x * (x + 1) // 2
    print(sum)