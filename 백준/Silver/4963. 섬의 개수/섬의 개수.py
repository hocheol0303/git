import sys
from collections import deque

def bfs(row, col):
    global lst, w, h
    d_row = [-1, -1, 0, 1, 1, 1, 0, -1]
    d_col = [0, 1, 1, 1, 0, -1, -1, -1]
    q = deque()
    q.append((row, col))
    lst[row][col] = '.'

    while q:
        row, col = q.popleft()
        for i in range(8):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0 <= n_row < h and 0 <= n_col < w and lst[n_row][n_col] == 1:
                lst[n_row][n_col] = '.'
                q.append((n_row, n_col))


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    else:
        count = 0
        lst = []
        for _ in range(h):
            lst.append(list(map(int, sys.stdin.readline().split())))
        for r in range(h):
            for c in range(w):
                if lst[r][c] == 1:
                    count += 1
                    bfs(r, c)
        print(count)