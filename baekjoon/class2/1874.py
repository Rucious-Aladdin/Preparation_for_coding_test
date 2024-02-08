N = int(input())
problem = []
for i in range(N):
    problem.append(int(input()))

#print(problem)    
    
stack = [1]
answer = ["+"]
previous_out = 0
is_success = True
count = 2

while len(problem) != 0 and is_success == True:
    next_out = problem.pop(0)
    #print(stack)
    #print(next_out)
    if len(stack) >= 1 and next_out == stack[-1]:
        previous_out = stack.pop()
        answer.append("-")
    else:
        if next_out > previous_out:
            while True:
                stack.append(count)
                answer.append("+")
                count += 1
                if stack[-1] == next_out:
                    previous_out = stack.pop()
                    answer.append("-")
                    break
        else:
            is_success = False
            break
    
        
if is_success:
    for a in answer:
        print(a)
else:
    print("NO")
        