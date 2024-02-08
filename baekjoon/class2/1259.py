nums =[]
while True:
    num = int(input())
    if num == 0:
        break
    nums.append(list(str(num)))

def panlindrome(strings):
    for i in range(len(strings) // 2):
        if strings[i] != strings[-(i + 1)]:
            return "no"
    return "yes"

for num in nums:
    print(panlindrome(num))