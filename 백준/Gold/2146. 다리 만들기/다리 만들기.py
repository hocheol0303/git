'''
한 턴을 다 돌고 확인했으면 함
반례:
    5
    1 0 0 0 1
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 1 0 0 1
'''

import sys
from collections import deque

def save_start(r, c):
    global lst, n, visited, save_q, color, color_map
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    color += 1

    q = deque([(r, c)])
    visited[r][c] = 0
    color_map[r][c] = color

    while q:
        row, col = q.popleft()
        color_map[row][col] = color
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0<=n_row<n and 0<=n_col<n and visited[n_row][n_col] == -1:
                if lst[n_row][n_col] == 0:
                    save_q.append((row, col))
                else:
                    visited[n_row][n_col] = 0
                    q.append((n_row, n_col))
    

def find_path(q):
    global n, lst, visited
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    min_ = float('inf')

    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0<=n_row<n and 0<=n_col<n:
                if visited[n_row][n_col] == -1:
                    visited[n_row][n_col] = visited[row][col] + 1
                    color_map[n_row][n_col] = color_map[row][col]
                    q.append((n_row, n_col))
                elif color_map[n_row][n_col] != color_map[row][col]:
                    if visited[n_row][n_col] == 0:
                        min_ = min(min_, visited[row][col])
                    else:
                        min_ = min(min_, visited[row][col] + visited[n_row][n_col])
    
    return min_

n = int(sys.stdin.readline())
lst = []
visited = [[-1]*n for _ in range(n)]
color_map = [[0]*n for _ in range(n)]
color = 0
save_q = deque()

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

for r in range(n):
    for c in range(n):
        if lst[r][c] == 1 and visited[r][c] == -1:
            save_start(r, c)

ans = find_path(save_q)
print(ans)

# for i in color_map:
#     print(i)

# print()
# for i in visited:
    # print(*i)
# print(save_q)

# while save_q:
#     row, col = save_q.popleft()
#     visited[row][col] = 1
# print()
# for i in visited:
#     print(*i)

