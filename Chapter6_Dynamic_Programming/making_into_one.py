X = int(input())

count_list = [30000] * 30001
count_list[1] = 0
for i in range(1, X+1):
    if (count_list[5 * i] > (count_list[i] + 1)) and (5 * i <= 30000):
        count_list[5 * i] = count_list[i] + 1
        
    if count_list[2 * i] > (count_list[i] + 1)  and (2 * i <= 30000):
        count_list[2 * i] = count_list[i] + 1
    
    if count_list[3 * i] > (count_list[i] + 1)  and (3 * i <= 30000):
        count_list[3 * i] = count_list[i] + 1
    
    if count_list[i + 1] > (count_list[i] + 1)  and (i+1 <= 30000):
        count_list[i + 1] = count_list[i] + 1


print(count_list[X])
print(count_list[:1000])