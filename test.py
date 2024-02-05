orders = [-1 for i in range(26)]
strings = list(input())

for i in range(len(strings)):
    if orders[ord(strings[i]) - 97] != -1:
        orders[ord(strings[i]) - 97] = i
for i in range(len(orders)):
    if i == len(orders) - 1:
        print(orders[i], end="")
    else:
        print(orders[i], end=" ")