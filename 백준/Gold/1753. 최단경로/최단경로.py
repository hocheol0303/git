import heapq
import sys

v, e = map(int,sys.stdin.readline().split())
graph={i+1:[] for i in range(v)}

start_node = int(sys.stdin.readline())
time = [float('inf')] * (v+1)

heap = [(0, start_node)]
time[start_node] = 0

for _ in range(e):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((weight, end))

# print(graph)

while heap:
    weight, end = heapq.heappop(heap)
    for n_weight, n_end in graph[end]:
        n_weight += weight
        if time[n_end] > n_weight:
            time[n_end] = n_weight
            heapq.heappush(heap, (n_weight, n_end))

for i in time[1:]:
    if i == float('inf'):
        print('INF')
    else:
        print(i)