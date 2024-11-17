# 촌수 계산: 트리

import sys
from collections import deque

def bfs(start, end):
    global grp, n
    q = deque()
    q.append(start)

    count = [0] * (n+1)

    while q:
        node = q.popleft()
        parent = grp[node]['parent']
        if parent != -1 and count[parent] == 0:
            q.append(parent)
            count[parent] = count[node] + 1
        for child in grp[node]['child']:
            if count[child] == 0:
                q.append(child)
                count[child] = count[node] + 1
        


    if count[end] == 0:
        print(-1)
    else:
        print(count[end])

n = int(sys.stdin.readline())
grp = {i:{'parent':-1, 'child':[]} for i in range(1, n+1)}

# 편의상 start, end
start, end = map(int, sys.stdin.readline().split())
numEdge = int(sys.stdin.readline())
for _ in range(numEdge):
    parent, child = map(int, sys.stdin.readline().split())
    grp[parent]['child'].append(child)
    grp[child]['parent'] = parent

# for i, info in grp.items():
#     print(i,info)

bfs(start, end)