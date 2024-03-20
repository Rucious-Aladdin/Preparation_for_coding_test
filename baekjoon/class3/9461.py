P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(90):
    P.append(P[-1] + P[-5])
    
TC = int(input())
indices = []
for i in range(TC):
    indices.append(int(input()))

for index in indices:
    print(P[index])