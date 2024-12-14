'''
마지막 돌을 가지는 사람이 진다.
1개 or 3개 가져갈 수 있다.
'''
import sys

n = int(sys.stdin.readline())
dp = [0] * (1001)

dp[1] = 'CY'
dp[2] = 'SK'
dp[3] = 'CY'

if n < 4:
    print(dp[n])
else:
    for i in range(4, n+1):
        if dp[i-1] == 'SK' or dp[i-3] == 'SK':
            dp[i] = 'CY'
        else:
            dp[i] = 'SK'
    print(dp[n])