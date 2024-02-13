N = int(input())
nums = list(map(int, input().split()))

disjoint_nums = list(set(nums))
disjoint_nums.sort()

dict = {}
for i in range(len(disjoint_nums)):
    dict[disjoint_nums[i]] = i

for num in nums:
    print(dict[num], end = " ")