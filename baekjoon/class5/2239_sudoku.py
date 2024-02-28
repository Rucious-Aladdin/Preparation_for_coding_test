nums = []
for i in range(9):
    num_str = list(input())
    num_str = [int(x) for x in num_str]
    nums.append(num_str)

positions = []
for i in range(9):
    for j in range(9):
        if nums[i][j] == 0:
            positions.append((i, j))
            
def check(nums, checknum, positions, current_pos):
    x, y = positions[current_pos]
    for b in range(0, 9):
        if b != y and nums[x][b] == checknum:
            return False
    for a in range(0, 9):
        if a != x and nums[a][y] == checknum:
            return False
    start_x = x - x % 3
    start_y = y - y % 3
    for i in range(3):
        for j in range(3):
            if start_x + i != x and start_y + j != y and\
                nums[start_x + i][start_y + j] == checknum:
                return False
    return True

def solve_sudoku(nums, positions, current_pos):
    if current_pos == len(positions):
        for l in nums:
            for x in l:
                print(x, end="")
            print()
        exit()
    else:
        x, y = positions[current_pos]
        for i in range(1, 10):
            nums[x][y] = i
            if check(nums, i, positions, current_pos):  
                solve_sudoku(nums, positions, current_pos + 1)
        #모두 False가 나왔으므로 0으로 되돌리고 리턴해야함.
        nums[x][y] = 0

solve_sudoku(nums, positions, 0)