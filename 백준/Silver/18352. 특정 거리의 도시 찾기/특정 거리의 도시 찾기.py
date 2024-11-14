import sys
from collections import deque

def bfs(start):
    global grp, distances
    q = deque()

    q.append(start)
    distances[start] = 0

    while q:
        start = q.popleft()
        for end in grp[start]:
            if distances[end] > distances[start]+1:
                distances[end] = distances[start]+1
                q.append(end)

n, m, k, x = map(int, sys.stdin.readline().split())

grp = {i:[] for i in range(1, n+1)}
distances = [float('inf')] * (n+1)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    grp[start].append(end)

# print(grp)
bfs(x)
# print(distances)
ans=[]
for i in range(1, n+1):
    if distances[i] == k:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    for i in sorted(ans):
        print(i)