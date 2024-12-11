import sys
from collections import deque

def bfs():
    global n, m, lst
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]
    visited = [[0]*m for _ in range(n)]
    count = [[float('inf')]*m for _ in range(n)]
    q = deque()

    q.append((0, 0))
    visited[0][0] = 1
    count[0][0] = 1

    while q:
        row ,col = q.popleft()
        for i in range(4):
            n_row, n_col = row + d_row[i], col + d_col[i]
            if 0 <= n_row < n and 0 <= n_col < m:
                # 방문 안한 길 방문
                if lst[n_row][n_col] == 0 and visited[row][col] == 1 and visited[n_row][n_col] == 0:
                    visited[n_row][n_col] = 1
                    count[n_row][n_col] = count[row][col] + 1
                    q.append((n_row, n_col))
                # 벽뚫: 벽 뚫은 적 없고 벽 만났을 때
                elif lst[n_row][n_col] == 1 and visited[row][col] == 1 and visited[n_row][n_col] == 0:
                    visited[n_row][n_col] = -1
                    count[n_row][n_col] = count[row][col] + 1
                    q.append((n_row, n_col))
                # 벽 뚫고 길 만났을 때
                elif lst[n_row][n_col] == 0 and (visited[row][col] == -1 or visited[row][col] == -2) and visited[n_row][n_col] == 0:
                    visited[n_row][n_col] = -2
                    count[n_row][n_col] = count[row][col] + 1
                    q.append((n_row, n_col))
                # 벽 뚫고 만난 길을 안뚫고 만났을 때
                elif lst[n_row][n_col] == 0 and visited[row][col] == 1 and visited[n_row][n_col] == -2:
                    # visited에 -2 속성 추가: 벽 뚫고 만난 "길"에는 -1 대신 -2를 줄 것. 이후 벽 안만나고 도착하면 수정
                    visited[n_row][n_col] = 1
                    count[n_row][n_col] = count[row][col] + 1
                    q.append((n_row, n_col))
        
        if visited[-1][-1] != 0:
            break
    
    if visited[-1][-1] == 0:
        print(-1)
    else:
        print(count[-1][-1])
        # for i in visited:
        #     print(i)

n, m = map(int, sys.stdin.readline().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, list(map(str, sys.stdin.readline().rstrip())))))

bfs()