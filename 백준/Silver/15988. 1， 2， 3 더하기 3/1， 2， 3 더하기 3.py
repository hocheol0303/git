import sys

tc = int(sys.stdin.readline())
dp = [0]*1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009
for _ in range(tc):
    n = int(sys.stdin.readline())
    print(dp[n])