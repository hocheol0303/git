'''
가중치, 점수를 고려

r이 거리가 아니죵 m으로 바꿨어요잉

visited에 정보 더 줘(거리)
'''

import sys
import heapq

def func(start):
    global grp, scores, n, m
    heap = []
    score = 0
    visited = [float('inf')]*(n+1)
    
    visited[start] = 0
    score += scores[start]

    for length, node in grp[start]:
        if length <= m:
            visited[node] = length
            score += scores[node]
            heapq.heappush(heap, (length, node))
    
    while heap:
        length, node = heapq.heappop(heap)

        for n_length, n_node in grp[node]:
            if n_length + length <= m and (visited[n_node] > length+n_length):
                if visited[n_node] == float('inf'):
                    score += scores[n_node]
                visited[n_node] = length+n_length
                heapq.heappush(heap, (n_length+length, n_node))

    return score

n, m, r = map(int, sys.stdin.readline().split())
grp = {i:[] for i in range(1, n+1)}
scores = [0]
scores.extend(map(int, sys.stdin.readline().split()))
max_score = 0

for _ in range(r):
    a, b, length = map(int, sys.stdin.readline().split())
    grp[a].append((length, b))
    grp[b].append((length, a))

for s in range(1, n+1):
    max_score = max(max_score, func(s))

# print(grp)
print(max_score)