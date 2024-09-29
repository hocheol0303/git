import sys
from collections import deque

def func():
    global d, shortcuts, dp
    q = deque()
    q.append(0)

    while q:
        start = q.popleft()
        if start >= d:
            continue
        if start in shortcuts.keys():
            for end, weight in shortcuts[start]:
                if dp[end] > dp[start]+weight:
                    dp[end] = dp[start]+weight
                    q.append(end)

        if dp[start+1] > dp[start]+1:
            dp[start+1] = min(dp[start+1], dp[start]+1)
            q.append(start+1)

n, d = map(int, sys.stdin.readline().split())

dp = [float('inf')]*(d+1)
dp[0] = 0
shortcuts = {}

for i in range(n):
    start, end, weight = map(int, sys.stdin.readline().split())
    if end > d:
        continue
    elif start not in shortcuts.keys():
        shortcuts[start] = [(end, weight)]
    else:
        shortcuts[start].append((end, weight))

func()
print(dp[-1])