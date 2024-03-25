# 데이터 입력 및 전처리
expression = input()
numbers = expression.split("+")
final_nums = []
for l in numbers:
    final_nums.extend(l.split("-"))
final_nums = [int(num) for num in final_nums]
expression = list(expression)
ops = []
for s in expression:
    if s == "+" or s == "-":
        ops.append(s)
#알고리즘
total_sum = final_nums.pop(0)
temp_sum = 0
parentheisFlag = False
while final_nums:
    cur_op = ops.pop(0)
    if parentheisFlag:
        if cur_op == "-":
            total_sum -= temp_sum
            temp_sum = final_nums.pop(0)
        else:
            temp_sum += final_nums.pop(0)            
    else:
        if cur_op == "-":
            temp_sum += final_nums.pop(0)
            parentheisFlag = True
        else:
            total_sum += final_nums.pop(0)
            parentheisFlag = False

if temp_sum != 0:
    total_sum -= temp_sum

print(total_sum)
            
        
