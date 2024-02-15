N = int(input())

a_to_i = {chr(i + ord("A")):i for i in range(26)}
a_to_i["."] = -1
i_to_a = {index:alphabet for alphabet, index in a_to_i.items()}

tree = [[] for i in range(N)]
for i in range(N):
    parent, node1, node2 = input().split()
    tree[a_to_i[parent]].append(a_to_i[node1])
    tree[a_to_i[parent]].append(a_to_i[node2])

def preorder(tree, root, i_to_a):
    if root != -1:
        print(i_to_a[root], end="")
    for i in tree[root]:
        if i != -1:
            preorder(tree, i, i_to_a)

def inorder(tree, root, i_to_a):
    if tree[root][0] != -1 and tree[root][0] != -1:
        inorder(tree, tree[root][0], i_to_a)
        print(i_to_a[root], end="")
        inorder(tree, tree[root][1], i_to_a)
    elif tree[root][0] == -1 and tree[root][1] != -1:
        print(i_to_a[root], end="")
        inorder(tree, tree[root][1], i_to_a)
    elif tree[root][0] != -1 and tree[root][1] == -1:
        inorder(tree, tree[root][0], i_to_a)
        print(i_to_a[root], end="")
    else:
        if root != -1:
            print(i_to_a[root], end="")
        
def postorder(tree, root, i_to_a):
    for i in tree[root]:
        if i != -1:
            postorder(tree, i, i_to_a)
    if root != -1:
        print(i_to_a[root], end="")

    
preorder(tree, 0, i_to_a)
print()
inorder(tree, 0, i_to_a)
print()
postorder(tree, 0, i_to_a)
