import sys
n, k = map(int, sys.stdin.readline().split())
dp = [float('inf')]*(k+1)

lst = []
for i in range(n):
    coin = int(sys.stdin.readline())
    if coin <= k:
        lst.append(coin)
lst.sort()

for i in lst:
    dp[i] = 1

# i원 만들고 다음칸
for target in range(1, k+1):
    for coin in lst:
        if target-coin >= 0:
            dp[target] = min(dp[target], dp[target-coin] + 1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])