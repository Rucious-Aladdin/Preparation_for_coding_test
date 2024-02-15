A, B, C = map(int, input().split())

binary_code = []

while B != 0:
    binary_code.append(B % 2)
    B = B // 2

quotients = [0 for i in range(len(binary_code))]
quotients[0] = A % C


for i in range(1, len(quotients)):
    quotients[i] = (quotients[i - 1] ** 2) % C
    
rest = -1
for i, bit in enumerate(binary_code):
    if bit == 1:    
        if rest == -1:
            rest = quotients[i]
        else:
            rest = (rest * quotients[i]) % C

print(rest)