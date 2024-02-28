notations = list(input())

answer = []
stack = []
priority_dict = {"+": 1, "-" : 1, "*" : 2, "/" : 2, "(":0}

#using prioirty tuple
for chr in notations:
    if chr == "+" or chr == "-" or chr == "/" or chr == "*":
        if len(stack) == 0:
            stack.append(chr)
        elif priority_dict[chr] <= priority_dict[stack[-1]]:
            while stack and priority_dict[chr] <= priority_dict[stack[-1]]:
                answer.append(stack.pop())
            stack.append(chr)
        elif priority_dict[chr] > priority_dict[stack[-1]]:
            stack.append(chr)
        pass
    elif chr == "(":
        stack.append(chr)
        pass
    elif chr == ")":
        x = stack.pop()
        while x != '(':
            answer.append(x)
            x = stack.pop()
    else:
        answer.append(chr)
        
while stack:
    answer.append(stack.pop())
    

print("".join(answer))