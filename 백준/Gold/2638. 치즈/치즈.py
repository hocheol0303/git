'''
2변 이상 공기 접촉 시 1시간 후 사라짐
내부는 공기 접촉 아닌 것으로 간주
맨 가장자리에는 치즈 놓지 않는다.
모든 치즈가 녹아 없어지는데 걸리는 시간

예시 input:
8 9 
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 0 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

시간이 좀 걸릴 것 같음

bfs로 벽 +1
for문으로 2면 이상 노출 벽 파괴

bfs로 벽 +1
for문으로 2면 이상 노출 벽 파괴

반복
'''

import sys
from collections import deque

def bfs(row, col):
    global lst, n, m, count
    visited = [[False]*m for _ in range(n)]
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    q = deque()
    q.append((row, col))

    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0 <= n_row < n and 0 <= n_col < m:
                # 길이면 방문
                if visited[n_row][n_col] == False and lst[n_row][n_col] == 0:
                    visited[n_row][n_col] = True
                    q.append((n_row, n_col))
                # 벽이면 +1
                if lst[n_row][n_col] != 0:
                    lst[n_row][n_col] += 1
                # 벽이고 2 면이 노출 -> 0 바꿔?
    
            


n, m = map(int, sys.stdin.readline().split())
lst = []
count = 0
time = 0
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    count += arr.count(1)
    lst.append(arr)

# for i in lst:
#     print(i)

# 내부 공간을 구분할 필요
# 최대 100x100 행렬

while count > 0:
    bfs(0,0)
    for r in range(n):
        for c in range(m):
            if lst[r][c] == 2:
                lst[r][c] = 1
            elif lst[r][c] > 2:
                lst[r][c] = 0
                count -= 1
    # print()
    # for i in lst:
    #     print(*i)
    time += 1

print(time)