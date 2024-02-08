N = int(input())
nums = list(map(int, input().split()))
M = int(input())
nums_answer = list(map(int, input().split()))
dict = {}

for i in range(len(nums)):
    try:
        dict[nums[i]] += 1
    except:
        dict[nums[i]] = 1

answer = []
for i in range(len(nums_answer)):
    try:
        answer.append(dict[nums_answer[i]])
    except:
        answer.append(0)

for ans in answer:
    print(ans, end = " ")