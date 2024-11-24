'''
d = (1, 0), (0, 1), (1, 1)

틀: 반례
4 3
0 0 0
0 2 0
1 0 0
9 0 0

틀: 풀고 보니 bfs - 시간초과
'''

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
lst = []
dp = [[0]*(m) for _ in range(n)]
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))
dp[0][0] = lst[0][0]

d = ((0,1), (1,0), (1,1))

for r in range(n):
    for c in range(m):
        for i in range(3):
            n_r, n_c = r+d[i][0], c+d[i][1]
            if 0 <= n_r < n and 0 <= n_c < m:
                dp[n_r][n_c] = max(dp[r][c]+lst[n_r][n_c], dp[n_r][n_c])
        
# for i in dp:
#     print(i)
print(dp[-1][-1])