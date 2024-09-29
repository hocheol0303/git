import sys
from collections import deque

def bfs(row, col):
    global n, m, lst, w, b
    color = lst[row][col]
    d_rows = [-1, 1, 0, 0]
    d_cols = [0, 0, -1, 1]
    q = deque()
    q.append((row, col))
    lst[row][col] = '.'
    mass = 1

    while q:
        row, col = q.popleft()

        for i in range(4):
            n_row = row + d_rows[i]
            n_col = col + d_cols[i]

            if n_row >= m or n_col >= n or n_row < 0 or n_col < 0:
                continue
            elif lst[n_row][n_col] != color:
                continue
            else:
                q.append((n_row, n_col))
                lst[n_row][n_col] = '.'
                mass += 1
    
    dct[color] += mass**2


n, m = map(int, sys.stdin.readline().split())
lst = []
w = b = 0
dct = {'W':0, 'B':0}
for _ in range(m):
    lst.append(list(map(str, sys.stdin.readline().rstrip())))

for r in range(m):
    for c in range(n):
        if lst[r][c] == '.':
            continue
        bfs(r, c)

print(dct['W'], dct['B'])