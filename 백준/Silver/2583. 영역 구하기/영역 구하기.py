'''
m, n, k
분리된 영역 개수, 넓이
'''

import sys
from collections import deque

def bfs(r, c):
    global lst, m, n
    q = deque()
    area = 0
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]

    q.append((r, c))
    lst[r][c] = 2
    area += 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            n_row, n_col = r+d_row[i], c+d_col[i]
            if 0 <= n_row < m and 0 <= n_col < n and lst[n_row][n_col] == 0:
                q.append((n_row, n_col))
                lst[n_row][n_col] = 2
                area += 1

    return area

m, n, k = map(int, sys.stdin.readline().split())
lst = [[0]*n for _ in range(m)]
box = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
areas = []

for c1, r1, c2, r2 in box:
    for r in range(r1, r2):
        for c in range(c1, c2):
            lst[r][c] = 1

for r in range(m):
    for c in range(n):
        if lst[r][c] == 0:
            areas.append(bfs(r, c))

# for i in lst:
#     print(i)
print(len(areas))
print(*sorted(areas))