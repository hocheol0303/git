'''
컨닝: 0 먼저 돌기(appendleft)
'''

import sys
from collections import deque

def bfs(start):
    global count, lst, n, m
    row, col = start
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]
    q = deque()
    q.append((row, col))


    while q:
        row, col = q.popleft()

        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0 <= n_row < m and 0 <= n_col < n:
                if lst[n_row][n_col] == 0:
                    if count[n_row][n_col] > count[row][col]:
                        count[n_row][n_col] = count[row][col]
                        q.appendleft((n_row, n_col))
                else:
                    if count[n_row][n_col] > count[row][col]+1:
                        q.append((n_row, n_col))
                        count[n_row][n_col] = count[row][col]+1

n, m = map(int, sys.stdin.readline().split())
lst=[]
count=[[float('inf')]*n for _ in range(m)]

for _ in range(m):
    lst.append(list(map(int, list(sys.stdin.readline().rstrip()))))

count[0][0] = 0
bfs((0,0))

# for i in lst:
#     print(i)
# print()
# for i in count:
#     print(i)

print(count[-1][-1])