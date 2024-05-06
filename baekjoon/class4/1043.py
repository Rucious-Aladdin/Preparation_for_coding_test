from collections import defaultdict, deque

def bfs(graphs, true_person_dict, true_person):
    visited = [False] * (N + 1)
    for x in true_person:
        visited[x] = True
    q = deque(true_person)
    
    while q:
        person = q.popleft()
        visited[person] = True
        
        for adj_person in graphs[person]:
            if not visited[adj_person]:
                visited[adj_person] = True
                q.append(adj_person)
    
    for i, x in enumerate(visited):
        if x:
            true_person_dict[i] = 1


N, M = map(int, input().split())
true_person = list(map(int, input().split()))
true_person.pop(0)

true_person_dict = defaultdict(int)
for x in true_person:
    true_person_dict[x] = 1

parties = []    
for i in range(M):
    ls = list(map(int, input().split()))
    ls.pop(0)
    parties.append(ls)
    
graphs = [[] for _ in range(N + 1)]
for party in parties:
    for x in party:
        if true_person_dict[x] == 1:
            for y in party:
                graphs[x].append(y)
                graphs[y].append(x)

bfs(graphs, true_person_dict, true_person)

count = 0
for party in parties:
    for x in party:
        if true_person_dict[x] == 1:
            break
    else:
        count+=1

print(count)