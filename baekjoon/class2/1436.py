N = int(input())
count = 0
start = 665
while True:
    start += 1
    if "666" in str(start):
        count += 1
    
    if count == N:
        print(start)
        break