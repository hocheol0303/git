'''
최단시간, 최단시간 개수
x+1, x-1, 2*x로 이동

3 0에서 3 1이 뜸 -> dp[n+1] > dp[n]+1 if문을 dp[n+1] >= dp[n]+1로 바꿈
0 0일 때 정답: 0 1, 내 답: 0 0
들여쓰기 이녀석아
'''

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
dp = [float('inf')]*100001
count = [0]*100001
q = deque()

q.append(n)
dp[n] = 0

while q:
    n = q.popleft()

    if n+1 <= 100000:
        if dp[n+1] >= dp[n]+1:
            dp[n+1] = dp[n]+1
            q.append(n+1)
    if n-1 >= 0:
        if dp[n-1] >= dp[n]+1:
            dp[n-1] = dp[n]+1
            q.append(n-1)
    if n*2 <= 100000:
        if dp[n*2] >= dp[n]+1:
            dp[n*2] = dp[n]+1
            q.append(n*2)
    
    if n == k:
        count[dp[k]] += 1

    # if dp[n]+1 <= 100000:
        # if n+1 == k:
        #     count[dp[n]+1] += 1
        # if n-1 == k:
        #     count[dp[n]+1] += 1
        # if n*2 == k:
        #     count[dp[n]+1] += 1

print(dp[k])
print(count[dp[k]])