'''
1. 끝 값 처리: n = 1일 때
2. 조건이 맞는데 더 가까이에 조건 맞는게 있을 때
    5
    1 8 2 3 9
'''
import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [0]*n
dp[0] = lst[0]
max_ = lst[0]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if lst[j] < lst[i]:
            dp[i] = max(lst[i] + dp[j], dp[i])
    if dp[i] == 0:
        dp[i] = lst[i]
    max_ = max(max_, dp[i])

# print(dp)
print(max_)