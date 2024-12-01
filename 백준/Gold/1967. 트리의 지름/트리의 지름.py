'''
1이 루트
컨닝: 
    1. 두 노드는 항상 리프노드일 것
    2. 루트에서 가장 먼 거리 찾고 거기서 먼 거리 찾기
    3. dfs -> bfs랑 시간은 똑같지 않나

key error: n = 1일 때 발생
'''
import sys
from collections import deque

def bfs(start):
    global grp, n
    costs = [float('inf')] * (n+1)
    visited = [False] * (n+1)
    visited[start] = True
    costs[start] = 0
    max_cost = 0
    saved_node = -1

    q = deque()
    q.append(start)

    while q:
        start = q.popleft()
        for next_node, cost in grp[start]:
            if visited[next_node]:
                continue
            else:
                visited[next_node] = True
                costs[next_node] = costs[start] + cost
                q.append(next_node)

                if max_cost < costs[next_node]:
                    max_cost = max(max_cost, costs[next_node])
                    saved_node = next_node

    # print(costs)
    return max_cost, saved_node


n = int(sys.stdin.readline())
grp = {i:[] for i in range(1, n+1)}
ans = 0

if n == 1:
    # _, _, _ = map(int, sys.stdin.readline().split())
    print(0)
else:
    for _ in range(n-1):
        parent, child, cost = map(int, sys.stdin.readline().split())
        grp[parent].append((child, cost))
        grp[child].append((parent, cost))

    # for s in range(1, n+1):
    #     ans = max(ans, bfs(s))

    _, target = bfs(1)
    ans, _ = bfs(target)

    # print(grp)
    print(ans)
