#매우 중요한 알고리즘, 투포인터의 가장 기초가 되는 알고리즘.
# 구간합보다 커지거나 같으면 -> 앞쪽의 start pointer를 계속 키우면서 구간 길이를 계속 갱신
# 구간합보다 작으면 -> end pointer를 키움 ...

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum_ = arr[0]
ans = 100001

while True:
    if sum_ < S:
        end += 1
        if end == N: break
        sum_ += arr[end]
    else:
        sum_ -= arr[start]
        ans = min(ans, end - start + 1)
        start += 1
        
print(ans if ans != 100001 else 0)