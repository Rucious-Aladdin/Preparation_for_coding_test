N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))
nums_paper = [0, 0]
size = N
off_pos = (0, 0)

def check(paper, off_pos, size, nums_paper):
    off_x, off_y = off_pos
    if size == 1:
        if paper[off_x][off_y] == 0:
            nums_paper[0] += 1
            return
        else:
            nums_paper[1] += 1
            return  
    else:
        start_color = paper[off_x][off_y]
        breakFlag = False
        for i in range(size):
            for j in range(size):
                if start_color != paper[off_x + i][off_y + j]:
                    size = size // 2
                    check(paper, (off_x, off_y), size, nums_paper)
                    check(paper, (off_x + size, off_y), size, nums_paper)
                    check(paper, (off_x, off_y + size), size, nums_paper)
                    check(paper, (off_x + size, off_y + size), size, nums_paper)
                    breakFlag = True
                    break
            if breakFlag:
                break
        else:
            nums_paper[start_color] += 1
            return
        
check(paper, off_pos, size, nums_paper)        
for paper_num in nums_paper:
    print(paper_num)