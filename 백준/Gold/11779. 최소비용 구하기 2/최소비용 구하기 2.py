import sys
import heapq

def func(s, e):
    global grp, n
    costs = [float('inf')] * (n+1)
    paths = [0]*(n+1)
    costs[start] = 0
    heap = [(0, start)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if cost > costs[node]:
            continue

        for next_cost, next_node in grp[node]:
            new_cost = cost + next_cost

            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                paths[next_node] = node
                heapq.heappush(heap, (new_cost, next_node))
    print(costs[e])
    route = [e]
    i = e
    while paths[i] != 0:
        route.append(paths[i])
        i = paths[i]

    print(len(route))
    print(*route[::-1])


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
grp = {i:[] for i in range(1, n+1)}

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    grp[start].append((cost, end))

start, end = map(int, sys.stdin.readline().split())

func(start, end)