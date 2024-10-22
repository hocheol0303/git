'''
depth를 정해줘야겠다
친구의 친구까지만
'''
import sys
from collections import deque

def bfs(start):
    global n, m, dct, visited
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        start, depth = q.popleft()
        if depth > 1:
            continue
        else:
            for i in dct[start]:
                if visited[i] == False:
                    visited[i] = True
                    q.append((i, depth+1))

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dct={i:[] for i in range(1, n+1)}
visited=[False]*(n+1)
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    if end not in dct[start]:
        dct[start].append(end)
        dct[end].append(start)

bfs(1)

# print(dct)
print(visited.count(True)-1)