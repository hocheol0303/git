'''
n, m, x : 학생 수, 길 수, 목적지

컨닝
'''

import sys
import heapq

def dijkstra(start):
    global x, costs
    s = start
    heap = []
    heapq.heappush(heap, (0, start))
    costs = [float('inf')]*(n+1)
    
    while heap:
        cost, start = heapq.heappop(heap)
        if costs[start] != float('inf'):
            continue
        else:
            costs[start] = cost
            if costs[start] < cost:
                continue
            else:
                for n_cost, dest in grp[start]:
                    if costs[dest] > cost+n_cost:
                        heapq.heappush(heap, (cost+n_cost, dest))
    
    if s == x:
        return costs
    return costs[x]

n, m, x = map(int, sys.stdin.readline().split())
grp = [[] for _ in range(n+1)]

come_cost = None
go_cost = [float('inf')]*(n+1)

for _ in range(m):
    start, dest, cost = map(int, sys.stdin.readline().split())
    grp[start].append((cost, dest))

for i in range(1, n+1):
    if i == x:
        come_cost = dijkstra(x)
    else:
        go_cost[i] = dijkstra(i)

max_ = 0
for i in range(1, n+1):
    if go_cost[i]+come_cost[i] == float('inf'):
        continue
    else:
        max_ = max(max_, go_cost[i]+come_cost[i])

# print(go_cost, come_cost)
print(max_)