#입력을 위한전형적인 소스코드

n = int(input())

data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

#빠르게 입력받는법

n, m, k = map(int, input().split())