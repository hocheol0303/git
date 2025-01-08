'''
n행 k열로 생각하기
'''

import sys
ans = 0

n, k = map(int, sys.stdin.readline().split())

dp = [[0]*201 for _ in range(201)]
for i in range(201):
    # k가 얼마이든 0은 하나(0, 00, 000, 0000, ...)
    dp[0][i] = 1
    dp[1][i] = i
    dp[i][1] = 1
    dp[i][2] = i+1

dp[0][0] = 0

for i in range(2, n+1):
    for j in range(3, k+1):
        for q in range(0, i+1):
            dp[i][j] += dp[q][j-1]

# for i in range(n+1):
#     print(dp[i][:k+1])

print(dp[n][k] % 1_000_000_000)