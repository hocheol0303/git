'''
앞 상자 크기가 뒷 상자 크기보다 작으면 뒤에 넣어
최대 상자 개수

1 2 3
 => 2번이 3번 들어갈 때 1번 빼
'''

import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [1]*n
before = [i for i in range(n)]

for i in range(n):
    for j in range(i, n):
        if lst[j] > lst[i]:
            if dp[j] < dp[i]+1:
                dp[j] -= dp[before[j]]
                dp[j] = dp[i]+1
                before[j] = i


print(max(dp))