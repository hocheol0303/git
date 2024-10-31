'''
1번 정점에서 n번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단경로로 이동하기

v1, v2 연결하고 start - v1 - v2 - end, 또는 start - v2 - v1 - end
start->v1 + v2->end  vs.  start->v2 + v1->end

start, end를 ans에 넣는 아주 멍청한 짓 함

weights[dest]에 방문하면 바로 나가기로 바꿈 -> 틀렸어
'''

import sys
import heapq

def find(start, end):
    global lst, n
    heap = []
    weights = [float('inf')] * (n+1)
    weights[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        weight, dest = heapq.heappop(heap)

        if weights[dest] < weight:
            continue

        weights[dest] = weight
        for n_weight, n_dest in lst[dest]:
            n_weight += weight
            if n_weight < weights[n_dest]:
                weights[n_dest] = n_weight
                heapq.heappush(heap, (n_weight, n_dest))


    return weights[end]

n, e = map(int,sys.stdin.readline().split())
lst = [[] for i in range(n+1)]

for _ in range(e):
    start, end, weight = map(int, sys.stdin.readline().split())
    to_end = weight, end
    to_start = weight, start
    
    if to_end not in lst[start]:
        lst[start].append(to_end)
        lst[end].append(to_start)

v1, v2 = map(int, sys.stdin.readline().split())

# v1, v2 연결하고 start - v1 - v2 - end, 또는 start - v2 - v1 - end
# start->v1 + v2->end  vs.  start->v2 + v1->end
ans = min(find(1,v1)+find(v2,n), find(1,v2)+find(v1,n)) + find(v1,v2)

# print(lst)
if ans == float('inf'):
    print(-1)
else:
    print(ans)