from collections import deque

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

def check_valid(maps, x, y):
    if (1 <= x <= len(maps)) and (1 <= y <= len(maps)):
        if maps[x-1][y-1] == 0:
            return True
    return False

def solution(board):
    visited = [[[False] * (len(board[0]) + 1) for i in range(len(board) + 1)] for j in range(2)]
    # 가로 기준 -> 오른쪽 점 (y축 2~N)
    # 세로기준 -> 아래쪽 점 (x축 2~N)
    # starts => 첫좌표, 두번째좌표, 상태(가로=0, 세로=1), 카운트
    starts = (1, 1, 1, 2, 0, 0) # (왼, 오) / (위, 아래)
    visited[starts[2]][starts[3]][0] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    fr_dx_s0 = [-1, -1, 0, 0]
    fr_dy_s0 = [+1, 0, 0, +1]
    sr_dx_s0 = [0, 0, +1, +1] 
    sr_dy_s0 = [0, -1, -1, 0]
    fr_dx_s1 = [0, 1, 0, 1]
    fr_dy_s1 = [-1, -1, 0, 0]
    sr_dx_s1 = [-1, 0, -1, 0] 
    sr_dy_s1 = [0, 0, 1, 1]

    q = deque([starts])
    N = len(board)
    while q:
        fx_cur, fy_cur, sx_cur, sy_cur, state, count = q.popleft()
        
        if (fx_cur == N and fy_cur == N) or (sx_cur == N and sy_cur == N) :
            return count
        
        # 4 movement types
        for i in range(4):
            fx_nx, fy_nx = fx_cur + dx[i], fy_cur + dy[i]
            sx_nx, sy_nx = sx_cur + dx[i], sy_cur + dy[i]
            
            if check_valid(board, fx_nx, fy_nx) and check_valid(board, sx_nx, sy_nx):
                if not visited[state][sx_nx][sy_nx]:
                    q.append((fx_nx, fy_nx, sx_nx, sy_nx, state, count + 1))
                    visited[state][sx_nx][sy_nx] = True               
        
        # 4 rotation type
        if state == 0:
            for j in range(4):
                fx_nx, fy_nx = fx_cur + fr_dx_s0[j], fy_cur + fr_dy_s0[j]
                sx_nx, sy_nx = sx_cur + sr_dx_s0[j], sy_cur + sr_dy_s0[j]
                if j < 2:
                    if check_valid(board, sx_cur-1, sy_cur-1) and check_valid(board, sx_cur-1, sy_cur):
                        if not visited[1][sx_nx][sy_nx]:
                            q.append((fx_nx, fy_nx, sx_nx, sy_nx, 1, count + 1))
                            visited[1][sx_nx][sy_nx] = True
                else:
                    if check_valid(board, sx_cur+1, sy_cur-1) and check_valid(board, sx_cur+1, sy_cur):
                        if not visited[1][sx_nx][sy_nx]:
                            q.append((fx_nx, fy_nx, sx_nx, sy_nx, 1, count + 1))
                            visited[1][sx_nx][sy_nx] = True
        elif state == 1:
            for j in range(4):
                fx_nx, fy_nx = fx_cur + fr_dx_s1[j], fy_cur + fr_dy_s1[j]
                sx_nx, sy_nx = sx_cur + sr_dx_s1[j], sy_cur + sr_dy_s1[j]
                if j < 2:
                    if check_valid(board, sx_cur-1, sy_cur-1) and check_valid(board, sx_cur, sy_cur-1):
                        if not visited[0][sx_nx][sy_nx]:
                            q.append((fx_nx, fy_nx, sx_nx, sy_nx, 0, count + 1))
                            visited[0][sx_nx][sy_nx] = True
                else:
                    if check_valid(board, sx_cur-1, sy_cur+1) and check_valid(board, sx_cur, sy_cur+1):
                        if not visited[0][sx_nx][sy_nx]:
                            q.append((fx_nx, fy_nx, sx_nx, sy_nx, 0, count + 1))
                            visited[0][sx_nx][sy_nx] = True
print(solution(board))