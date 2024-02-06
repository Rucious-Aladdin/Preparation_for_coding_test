N = int(input())
digits = list(str(N))

sum1 = 0
sum2 = 0
for i in range(len(digits) // 2):
    sum1 += int(digits[i])
    sum2 += int(digits[-(i + 1)])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")