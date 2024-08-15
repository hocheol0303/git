import sys
from collections import deque
t = int(sys.stdin.readline())

def bfs(lst, row, col):
    global m, n
    q = deque()
    q.append([row,col])

    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]


    while q:
        row, col = q.popleft()
        lst[row][col] = 0

        for i in range(4):
            n_row = row + d_row[i]
            n_col = col + d_col[i]
            if n_row >= n or n_col >= m or n_row < 0 or n_col < 0:
                continue
            if lst[n_row][n_col] == 1:
                lst[n_row][n_col] = 0
                q.append([n_row, n_col])
            
            





    
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    lst = [[0]*m for i in range(n)]

    count=0

    for i in range(k):
        col, row = map(int, sys.stdin.readline().split())
        lst[row][col] = 1

    # for i in lst:
    #     print(i)

    if k == 1:
        print(1)
        continue
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1:
                count+=1
                bfs(lst, i, j)
    print(count)