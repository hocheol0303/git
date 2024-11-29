import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    for j in range(i+1, i+lst[i]+1):
        if j >= n:
            break
        dp[j] = min(dp[j], dp[i]+1)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])