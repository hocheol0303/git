'''
감도 안잡힘
bfs
벽을 세우는 백트래킹
백트래킹으로 벽 세우고 3개에서 bfs로 바이러스 퍼뜨리고 0 개수 확인 -> 개수 max 찾기

약간 브루트포스향 나는 백트래킹
많이 신기해용
'''

import sys
from collections import deque
import copy

def virus():
    global n, m, lst, result
    q = deque()
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]

    n_lst = copy.deepcopy(lst)
    
    for i in range(n):
        for j in range(m):
            if n_lst[i][j] == 2:
                q.append((i, j))

    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row = row + d_row[i]
            n_col = col + d_col[i]
            if n_row >= n or n_row < 0 or n_col >= m or n_col < 0: continue
            elif n_lst[n_row][n_col] == 0:
                n_lst[n_row][n_col] = 2
                q.append((n_row, n_col))
    
    count = 0

    for i in range(n):
        count+=n_lst[i].count(0)

    result = max(result, count)


# 백트래킹 함수
def dfs(cnt):
    global lst
    if cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0:
                lst[i][j] = 1
                dfs(cnt+1)
                lst[i][j] = 0

n, m = map(int, sys.stdin.readline().split())
lst = []
result = 0
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

dfs(0)
print(result)