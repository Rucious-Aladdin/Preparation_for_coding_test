N = int(input())

stages = [1]

d = 6
current = 1
count = 1
while True:
    if current >= N:
        break
    
    current += d
    stages.append(current)
    d += 6
    count += 1
    
print(count)