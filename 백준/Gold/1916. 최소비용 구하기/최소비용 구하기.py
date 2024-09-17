import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([cost, end])

start_node, end_node = map(int, sys.stdin.readline().split())

heap = [(0, start_node)]
time = [float('inf')] * (n+1)

while heap:
    cost, end = heapq.heappop(heap)
    if time[end] != float('inf'):
        continue
    else:
        time[end] = cost

        for n_cost, n_end in graph[end]:
            n_cost += cost
            heapq.heappush(heap, [n_cost, n_end])

print(time[end_node])