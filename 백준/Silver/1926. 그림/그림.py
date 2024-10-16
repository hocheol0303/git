import sys
from collections import deque

def bfs(row, col):
    global max_, lst, count
    q = deque()
    q.append((row, col))
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]
    cnt=1
    lst[row][col] = '.'
    count[row][col]=1
    
    while q:
        row, col = q.popleft()

        for i in range(4):
            n_row = row+d_row[i]
            n_col = col+d_col[i]

            if 0 <= n_row < n and 0 <= n_col < m:
                if lst[n_row][n_col] == 1 and count[n_row][n_col] == 0:
                    count[n_row][n_col] = 1
                    cnt+=1
                    lst[n_row][n_col] = '.'
                    q.append((n_row, n_col))

    max_ = max(max_, cnt)

n, m = map(int, sys.stdin.readline().split())
lst = []
count = [[0]*m for i in range(n)]
num = 0
max_ = 0
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            bfs(i, j)
            num+=1

print(num)
print(max_)