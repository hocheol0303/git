'''
다른 모든 회원과 친구이면(1층) 1점
모든 회원과 친구(1층), 친구의 친구(2층)이면 2점
점수 오름차순 전부
'''

import sys
from collections import deque

def bfs(s):
    global dct, lst, n
    q = deque()

    visited = [False]*(n+1)
    start = s
    depth = 0
    visited[start]=True
    q.append((start, depth))

    max_depth = 0
    while q:
        start, depth = q.popleft()
        max_depth = max(max_depth, depth)

        for i in dct[start]:
            if visited[i]:
                continue
            else:
                q.append((i, depth+1))
                visited[i] = True
    
    lst[s][1] = max_depth
    


n = int(sys.stdin.readline())
dct = {i:[] for i in range(1, n+1)}
lst = [[i,0] for i in range(n+1)]       # 0번이 회원번호 1번이 점수

while True:
    node1, node2 = map(int, sys.stdin.readline().split())
    if node1 == -1 and node2 == -1:
        break
    else:
        dct[node1].append(node2)
        dct[node2].append(node1)

for i in range(1, n+1):
    bfs(i)

lst.sort(key=lambda x:x[1])

min_score = lst[1][1]
bosses = []

for num, score in lst[1:]:
    if score != min_score:
        break
    else:
        bosses.append(num)

print(min_score, len(bosses))
print(*bosses)