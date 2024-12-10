'''
칸 안에 늑대보다 양이 많으면 양 이겨 나머지 늑대 이겨
. # v o 있음
'''

import sys
from collections import deque

def bfs(row, col):
    global visited, lst, r, c, ans
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]
    q = deque()
    sheep = 0
    wolves = 0

    visited[row][col] = True
    q.append((row, col))
    if lst[row][col] == 'v':
        wolves += 1
    elif lst[row][col] == 'o':
        sheep += 1

    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row, n_col = row + d_row[i], col + d_col[i]
            if 0 <= n_row < r and 0 <= n_col < c:
                if visited[n_row][n_col] == False and lst[n_row][n_col] != '#':
                    visited[n_row][n_col] = True
                    if lst[n_row][n_col] == 'v':
                        wolves += 1
                    elif lst[n_row][n_col] == 'o':
                        sheep += 1
                    q.append((n_row, n_col))
    
    if sheep > wolves:
        ans[0] += sheep
    else:
        ans[1] += wolves



r, c = map(int, sys.stdin.readline().split())
visited = [[False] * c for _ in range(r)]
lst = []
ans = [0, 0]
for _ in range(r):
    lst.append(list(map(str, sys.stdin.readline().rstrip())))

# for i in lst:
#     print(i)

for i in range(r):
    for j in range(c):
        if visited[i][j] == False and lst[i][j] != '#':
            bfs(i, j)

print(*ans)