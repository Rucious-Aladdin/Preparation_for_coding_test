N,M,K =map(int, input().split())
numbers = list(map(int, input().split()))

print(N, M, K)
print(numbers)

numbers.sort(reverse=True)
print(numbers)

sum = numbers[0] * K + numbers[1]
length = K + 1

answer = sum * (M // (K+1)) + numbers[0] * (M % (K+1))
print(answer)

# 가장 큰 수 가 등장하는 횟수를 미리계산해서 시간단축!