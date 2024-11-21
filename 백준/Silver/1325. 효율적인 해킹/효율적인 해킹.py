'''
a가 b를 신뢰하면 b를 해킹했을 때 a도 해킹할 수 있다.
한 번에 가장 많이 해킹할 수 있는 컴퓨터의 번호를 오름차순 출력

부모노드가 자식노드를 신뢰함 -> 깊이 문제
'''

import sys
from collections import deque

def bfs(start):
    global grp, n
    q = deque()
    visited = [0]*(n+1)

    count = 1
    q.append(start)
    visited[start] = 1

    while q:
        start = q.popleft()
        for i in grp[start]:
            if visited[i] == 0:
                count+=1
                q.append(i)
                visited[i] = 1
    
    return count

n, m = map(int, sys.stdin.readline().split())
grp = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    grp[b].append(a)

max_ = 0
ans = []
for i in range(1, n+1):
    cnt = bfs(i)
    if max_ < cnt:
        ans.clear()
        ans.append(i)
        max_ = cnt
    elif max_ == cnt:
        ans.append(i)

# print(cnt)

print(*ans)