import sys
n = int(sys.stdin.readline())

lst = [0]*(n+1)
dp = [0]*(n+1)

for i in range(1, n+1):
    lst[i] = int(sys.stdin.readline())

if n > 2:
    dp[1] = lst[1]
    dp[2] = dp[1]+lst[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], lst[i]+dp[i-2], lst[i]+lst[i-1]+dp[i-3])
    
    # print(lst)
    # print(dp)
    print(dp[-1])
else:
    print(sum(lst))