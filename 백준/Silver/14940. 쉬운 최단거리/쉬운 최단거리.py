import sys
from collections import deque

def bfs(lst, cnt, row, col):
    cnt[row][col] = 0
    q = deque()
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]

    q.append([row,col])

    while q:
        row, col = q.popleft()
        lst[row][col] = '.'
        for i in range(4):
            n_row = row + d_row[i]
            n_col = col + d_col[i]

            if n_row<0 or n_col < 0 or n_row >= n or n_col >= m :
                continue
            if lst[n_row][n_col] == '.':
                if cnt[n_row][n_col] > cnt[row][col] + 1:
                    cnt[n_row][n_col] = cnt[row][col]+1
                    q.append([n_row, n_col])
            elif lst[n_row][n_col] != 0 and cnt[n_row][n_col] > cnt[row][col] + 1:
                cnt[n_row][n_col] = cnt[row][col] + 1
                q.append([n_row, n_col])
        
        # print()
        # for i in cnt:
        #     print(i)

n, m = map(int, sys.stdin.readline().split())

lst = []
cnt = [[1000000]*m for i in range(n)]
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

for row in range(n):
    for col in range(m):
        if lst[row][col] == 2:
            bfs(lst, cnt, row, col)
            break
for row in range(n):
    for col in range(m):
        if lst[row][col] == 0:
            cnt[row][col] = 0
        elif lst[row][col] == 1:
            cnt[row][col] = -1

# for i in lst:
#     print(i)
# print()
# for i in cnt:
#     print(i)

for i in cnt:
    print(*i)