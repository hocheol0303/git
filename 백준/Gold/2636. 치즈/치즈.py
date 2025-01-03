'''
가장자리엔 치즈가 없다 -> 이 정보를 가지고 가장자리에서 bfs 출발하면 바깥인지 알 수 있셔

1. 치즈가 모두 녹아서 없어지는 데 걸리는 시간 출력
2. 모두 녹기 한 시간 전에 남아있는 치즈 조각 수 출력
'''
import sys
from collections import deque

def bfs():
    global lst, n, m, cheese
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    visited = [[0]*m for _ in range(n)]
    melt_num = 0

    q = deque([(0,0)])
    visited[0][0] = 1

    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0<=n_row<n and 0<=n_col<m and visited[n_row][n_col] == 0:
                visited[n_row][n_col] = 1
                if lst[n_row][n_col] == 0:
                    q.append((n_row, n_col))
                elif lst[n_row][n_col] == 1:
                    melt_num += 1
    
    for r in range(n):
        for c in range(m):
            if visited[r][c] == lst[r][c]:
                lst[r][c] = 0

    if cheese != melt_num:
        cheese -= melt_num
        return None
    else:
        return melt_num


lst = []
n, m = map(int, sys.stdin.readline().split())
cheese = 0
hours = 0

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    cheese += row.count(1)
    lst.append(row)

while True:
    ans = bfs()
    hours += 1
    if ans:
        break
    else:
        continue

print(hours)
print(ans)