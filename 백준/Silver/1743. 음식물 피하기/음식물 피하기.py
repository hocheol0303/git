import sys
from collections import deque

def bfs(r, c):
    global lst, n, m
    q = deque()
    q.append((r, c))
    size = 1
    lst[r][c] = 0

    d_r = [-1, 1, 0, 0]
    d_c = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            n_r, n_c = r+d_r[i], c+d_c[i]
            if 0 <= n_r < n and 0 <= n_c < m and lst[n_r][n_c] == 1:
                size += 1
                lst[n_r][n_c] = 0
                q.append((n_r, n_c))
    
    return size

n, m, k = map(int, sys.stdin.readline().split())
lst = [[0]*m for _ in range(n)]
max_size = 0

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    lst[r-1][c-1] = 1

# for i in lst:
#     print(i)

for r in range(n):
    for c in range(m):
        if lst[r][c] == 1:
            max_size = max(max_size, bfs(r, c))

print(max_size)