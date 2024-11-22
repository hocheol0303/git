'''
LIS: i 키우면서 되돌아보는 j - lst[i] > lst[j] -> dp[i] = max(dp[i], dp[j]+1)
'''

import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
ascend_dp = [1] * n
descend_dp = [0] * n

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            ascend_dp[i] = max(ascend_dp[i], ascend_dp[j]+1)

# 뒤에서부터 내려오면서 커지는지 확인
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if lst[i] > lst[j]:
            descend_dp[i] = max(descend_dp[i], descend_dp[j]+1)

ans = 0
for i in range(n):
    ans = max(ans, descend_dp[i]+ascend_dp[i])
print(ans)