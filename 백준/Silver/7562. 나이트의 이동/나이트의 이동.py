'''
12시 방향부터 시계
d_row = [-2, -1, 1, 2, 2, 1, -1, -2]
d_col = [1, 2, 2, 1, -1, -2, -2, -1]
'''

import sys
from collections import deque

def bfs(l, start_row, start_col, dest_row, dest_col):
    global lst
    d_row = [-2, -1, 1, 2, 2, 1, -1, -2]
    d_col = [1, 2, 2, 1, -1, -2, -2, -1]
    q = deque()
    q.append((start_row, start_col))

    while q:
        row, col = q.popleft()
        
        for i in range(8):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0 <= n_row < l and 0 <= n_col < l:
                if lst[n_row][n_col] == 0:
                    lst[n_row][n_col] = lst[row][col]+1
                    q.append((n_row, n_col))

        if lst[dest_row][dest_col] != 0:
            print(lst[dest_row][dest_col])
            break

tc = int(sys.stdin.readline())
for _ in range(tc):
    l = int(sys.stdin.readline())
    lst = [[0]*l for i in range(l)]

    start = tuple(map(int, sys.stdin.readline().split()))
    dest = tuple(map(int, sys.stdin.readline().split()))
    if start == dest:
        print(0)
    else:
        bfs(l, *start, *dest)