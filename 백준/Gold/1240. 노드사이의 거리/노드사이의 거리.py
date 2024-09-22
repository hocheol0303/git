import sys
import heapq
n, m = map(int,sys.stdin.readline().split())
grp={i+1:[] for i in range(n)}


for i in range(n-1):
    start, end, distance = map(int,sys.stdin.readline().split())
    grp[start].append((distance, end))
    grp[end].append((distance, start))

for i in range(m):
    cost=[float('inf')]*(n+1)
    new_grp= grp.copy()
    heap=[]
    start, end = map(int, sys.stdin.readline().split())

    for item in grp[start]:
        heapq.heappush(heap, item)
    
    while cost[end] == float('inf'):
        distance, target = heapq.heappop(heap)
        cost[target] = distance

        for new_distance, new_target in grp[target]:
            new_distance += distance
            if new_distance < cost[new_target]:
                heapq.heappush(heap, (new_distance, new_target))
            else:
                continue
    
    print(cost[end])