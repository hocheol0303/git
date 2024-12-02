'''
먼저번의 트리 지름이랑 똑같애?
어떤 한 노드에서 가장 먼 노드 잡고 >>> 이게 항상 그러한지? 일단 예제에선 됐음
그 노드에서 가장 먼 노드까지의 거리가 트리의 지름?
'''

import sys
from collections import deque

def bfs(node):
    global grp, n
    q = deque()
    dist = [float('inf')] * (n+1)

    dist[node] = 0
    q.append(node)
    ans_node = node

    while q:
        node = q.popleft()

        for new_node, new_cost in grp[node]:
            if dist[new_node] == float('inf'):
                dist[new_node] = dist[node] + new_cost
                q.append(new_node)
                if dist[new_node] > dist[ans_node]:
                    ans_node = new_node
    
    return ans_node, dist[ans_node]



n = int(sys.stdin.readline())
grp = {i:[] for i in range(1, n+1)}

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    node = lst[0]

    for i in range(1, len(lst), 2):
        if lst[i] == -1:
            break
        else:
            grp[node].append((lst[i], lst[i+1]))

ans_node, _ = bfs(1)
_, ans_cost = bfs(ans_node)

print(ans_cost)