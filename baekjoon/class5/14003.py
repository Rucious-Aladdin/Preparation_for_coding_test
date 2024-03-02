N = int(input())
sequences = list(map(int, input().split()))
dp_table = [1 for i in range(N)]
prev_table = [-1 for i in range(N)]


for i in range(N):
    max_value = 0
    max_index = -1
    for j in range(0, i - 1):
        if dp_table[j] > max_value and sequences[j] < sequences[i]:
            max_value = dp_table[j]
            max_index = j
    dp_table[i] = max_value + 1
    prev_table[i] = max_index

answer = []
end_node = dp_table.index(max(dp_table))
while True:
    answer.insert(0, sequences[end_node])
    end_node = prev_table[end_node]
    
    if end_node == -1:
        break
print(prev_table)
print(dp_table)    