X = list(input())
X.sort()

sum = 0
for i in range(len(X)):
    if ord(X[i]) <= 57 and ord(X[i]) >= 48:
        sum += int(X[i])
        last = i

#join을애용하자! - list보다 속도가 훨씬 빠르다.
ans_str = "".join(X[last + 1:])

print(ans_str + str(sum))        