'''
n보다 크거나 같으면 push

for i in range(n):
    count = [[0]*n for _ in range(n)]

위 코드면 재생성이래 초기화가 아닌건가? -> 이거때문에 메모리 초과?
큐에 담기는거 안겹치게
'''

import sys
from collections import deque

def bfs(row, col):
    global lst, count, n, height

    q = deque()
    q.append((row, col))
    d_row, d_col = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        row, col = q.popleft()
        count[row][col] = 1
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0 <= n_row < n and 0 <= n_col < n:
                if lst[n_row][n_col] > height and count[n_row][n_col] == 0:
                    q.append((n_row, n_col))
                    count[n_row][n_col] = 1



n = int(sys.stdin.readline())
lst=[]
max_height = 0
min_height = float('inf')
max_ = 0
count = [[0]*n for _ in range(n)]

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))
    max_height = max(max_height, max(lst[-1]))
    min_height = min(min_height, min(lst[-1]))



for height in range(min_height-1, max_height+1):
    cnt = 0
    for i in range(n):
        for j in range(n):
            count[i][j] = 0

    for r in range(n):
        for c in range(n):
            if lst[r][c] > height and count[r][c] == 0:
                bfs(r, c)
                cnt += 1
    max_ = max(max_, cnt)

    # for i in count:
    #     print(i)
    # print()

print(max_)