'''
두 방향 중 하나로 정하면 그 방향으로만 k칸 갈 수 있다.

dp + bfs 하니까 메모리아웃 -> bfs 빼보자
'''

import sys

n = int(sys.stdin.readline())
lst = []
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

d_r = [0, 1]
d_c = [1, 0]

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))


for r in range(n):
    for c in range(n):
        if r == n-1 and c == n-1:
            break
        for i in range(2):
            n_r, n_c = r+d_r[i]*lst[r][c], c+d_c[i]*lst[r][c]
            if 0 <= n_r < n and 0 <= n_c < n:
                dp[n_r][n_c] += dp[r][c]

# for i in dp:
#     print(i)
print(dp[-1][-1])