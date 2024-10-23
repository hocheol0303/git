'''
연속된 몇 개의 수
'''

import sys

n = int(sys.stdin.readline())
max_ = -float('inf')

lst = [0]
lst.extend(list(map(int, sys.stdin.readline().split())))
dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = max(lst[i]+dp[i-1], lst[i])
    max_ = max(max_, dp[i])
    
# print(dp)
# print(lst)
print(max_)