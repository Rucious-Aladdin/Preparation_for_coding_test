N,M,K =map(int, input().split())
numbers = list(map(int, input().split()))

print(N, M, K)
print(numbers)

numbers.sort(reverse=True)
print(numbers)

answer=0
in_flag = True

while(M >= K):
    if(in_flag==True):
        M -= K
        answer += K * numbers[0]
        in_flag=False
    else:
        M -= 1
        answer += numbers[1]
        in_flag=True

if (in_flag == True):
    answer += M * numbers[0]
else:
    answer +=  numbers[1] + (M - 1) * numbers[0]
    
print(answer)

## 주어진 시간 30분, 남은 시간 11분 36초, 
## 소요시간 18분 24초

