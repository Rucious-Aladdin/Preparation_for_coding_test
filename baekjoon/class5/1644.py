from itertools import combinations

N = int(input())
isprime = [1] * (N + 1)

isprime[0] = 0
isprime[1] = 0
start = 2

while start != N + 1:
    if isprime[start] == 1:
        for i in range(1, (N // start + 1)):
            if i != 1:
                isprime[i * start] = 0
    start += 1

prime_num_list = []
for i, x in enumerate(isprime):
    if x == 1:
        prime_num_list.append(i)

#합이 S인 구간합 찾기?
start = 0
end = 0
sum = 0
count = 0
while end < len(prime_num_list):
    if sum < N:
        sum += prime_num_list[end]
        end += 1
    while sum >= N:
        if sum == N:
            count += 1
        sum -= prime_num_list[start]
        start += 1
print(count)