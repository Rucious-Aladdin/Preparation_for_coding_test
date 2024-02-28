from itertools import combinations

N, M = map(int, input().split())

houses = []
stores = []
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            houses.append((i, j))
        elif maps[i][j] == 2:
            stores.append((i, j))

stores_comb = []
for i in combinations(stores, M):
    stores_comb.append(list(i))
    
min_cost = 1e9
for combs in stores_comb:
    distance = [1e9] * len(houses)
    for store_pos in combs:
        for i in range(len(houses)):
            mahattan_dist = abs(houses[i][0] - store_pos[0]) + abs(houses[i][1] - store_pos[1])
            if distance[i] > mahattan_dist:
                distance[i] = mahattan_dist
    if min_cost > sum(distance):
        min_cost = sum(distance)
print(min_cost)