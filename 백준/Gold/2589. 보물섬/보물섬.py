'''
어떻게 빨리하지 생각했는데 걍 브루트포스로 푸는거였어..
bfs 시간복잡도 계산하는거 좀 찾아봐야겠네
'''

import sys
from collections import deque

def bfs(r, c):
    global n, m, lst
    visited = [[0]*m for _ in range(n)]
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]

    q = deque([(r,c)])
    visited[r][c] = 1
    max_ = visited[r][c] - 1

    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0<=n_row<n and 0<=n_col<m:
                if lst[n_row][n_col] == 'L' and visited[n_row][n_col] == 0:
                    visited[n_row][n_col] = visited[row][col] + 1
                    max_ = max(max_, visited[n_row][n_col] - 1)
                    q.append((n_row, n_col))

    return max_

n, m = map(int, sys.stdin.readline().split())
lst = []
max_length = 0

for _ in range(n):
    lst.append(list(map(str, sys.stdin.readline().rstrip())))

for r in range(n):
    for c in range(m):
        if lst[r][c] == 'L':
            max_length = max(bfs(r, c), max_length)

print(max_length)
# for i in lst:
#     print(i)