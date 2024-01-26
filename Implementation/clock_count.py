def check(H, M, S):
    if (H == 3):
        return True
    nums = [(M // 10), (M % 10), (S // 10), (S % 10)]
    if 3 in nums:
        return True
    return False

N = int(input()) + 1
hour, minute, sec = 0, 0, 0
count = 0

for i in range(N * 60 * 60):
    hour = i // 3600
    i -= hour * 3600
    minute = i // 60
    i -= minute * 60
    sec = i
    print(hour, minute, sec)
    if(check(hour,minute,sec)):
        count += 1

print(count)