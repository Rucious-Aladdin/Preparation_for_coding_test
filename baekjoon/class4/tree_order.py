import sys
input=sys.stdin

n=int(input.readline())
dic={}

# 딕셔너리를 이용한 트리구축
for i in range(n):
    root, left, right = map(str, input.readline().strip().split(" "))
    dic[root]=[left,right]
#함수 바깥에 변수정의
ans=""
def preorder(r):
    #변수를 글로벌 타입으로 재정의함.
    global ans
    ans+=r
    if dic[r][0] != ".":
        preorder(dic[r][0])
    if dic[r][1] != ".":
        preorder(dic[r][1])
def postorder(r):
    global ans
    if dic[r][0] != ".":
        postorder(dic[r][0])
    ans+=r               
    if dic[r][1] != ".":
        postorder(dic[r][1])
def inorder(r):
    global ans
    if dic[r][0] != ".":
        inorder(dic[r][0])

    if dic[r][1] != ".":
        inorder(dic[r][1])
    ans+=r
preorder("A")
ans+="\n"
postorder("A")
ans+="\n"
inorder("A")
print(ans)
