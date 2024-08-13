'''
정점 개수 n, 간선 개수 m
m개 줄에 연결정보

몇 덩어리?

시간초과: 갔던 데는 넣지말기
'''
import sys
from collections import deque

def bfs(idx):
    global vertex, visited, count
    q = deque()
    q.append(idx)

    while q:
        idx = q.popleft()
        if visited[idx] == 0:
            visited[idx] = count

        for i in vertex[idx]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = count
    count +=1


n, m = map(int, sys.stdin.readline().split())
vertex = {i+1:[] for i in range(n)}
visited = [0 for i in range(n+1)]
count=1
for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    vertex[start].append(end)
    vertex[end].append(start)

# print(vertex)
# print(visited)

for i in range(1, n+1):
    if visited.count(0) == 1:
        break
    bfs(i)
    # print(visited)


print(len(set(visited))-1)