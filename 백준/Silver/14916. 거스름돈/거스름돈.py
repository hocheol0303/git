'''
2원, 5원으로 최소
'''

import sys
n = int(sys.stdin.readline())
dp = [float('inf')] * (100001)


dp[2] = 1
dp[4] = 2
dp[5] = 1
dp[6] = 3

for i in range(7, n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1

print(dp[n]) if dp[n] != float('inf') else print(-1)