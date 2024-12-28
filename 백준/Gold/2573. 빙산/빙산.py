'''
두 덩어리 이상으로 분리되는 최초의 시간 출력
이미 다 녹아내렸으면 0 출력
'''
import sys
from collections import deque

# 이중 반복문에 넣어서 빙산 덩어리 탐색할 것
def bfs(r, c, iceberg_number):
    global n, m, lst, visited
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]

    q = deque([(r,c)])
    visited[r][c] = iceberg_number

    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0<=n_row<n and 0<=n_col<m:
                if lst[n_row][n_col] != 0 and visited[n_row][n_col] == 0:
                    visited[n_row][n_col] = iceberg_number
                    q.append((n_row,n_col))

# 주위 바다만큼 빙산 녹일 것
def melt():
    global n, m, lst
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    copy = [[0]*m for _ in range(n)]
    exist_iceberg = False

    for r in range(n):
        for c in range(m):
            if lst[r][c] != 0:
                exist_iceberg = True
                for i in range(4):
                    n_row, n_col = r+d_row[i], c+d_col[i]
                    if 0<=n_row<n and 0<=n_col<m:
                        if lst[n_row][n_col] == 0:
                            copy[r][c] += 1
    
    # False면 이미 다 녹아서 없는겨
    if exist_iceberg == False:
        return exist_iceberg
    else:
        for r in range(n):
            for c in range(m):
                lst[r][c] = max(0, lst[r][c] - copy[r][c])

        return exist_iceberg

n, m = map(int, sys.stdin.readline().split())
lst = []
count = 0
hihi = False
iceberg_number = 0

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

while True:
    iceberg_number = 0
    visited = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if lst[r][c] != 0 and visited[r][c] == 0:
                iceberg_number += 1
                bfs(r,c,iceberg_number)

    if iceberg_number >= 2:
        print(count)
        break
    else:
        count += 1
        check = melt()
        # melt에서 영향을 받은 빙산이 있으면 True, 없으면(이미 다 녹음) False 저장
        if check:
            continue
        else:
            print(0)
            break
