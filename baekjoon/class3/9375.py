TC = int(input())
answers = []
for i in range(TC):
    cloth_num = int(input())
    cloth_dict = {}
    if cloth_num == 0:
        answers.append(0)
        continue
    else:
        for i in range(cloth_num):
            _, cloth_type = input().split()
            if cloth_type in cloth_dict:
                cloth_dict[cloth_type] += 1
            else:
                cloth_dict[cloth_type] = 1
        product = 1
        for _ , value in cloth_dict.items():
            product *= (value + 1)
        answers.append(product - 1)

for answer in answers:
    print(answer)