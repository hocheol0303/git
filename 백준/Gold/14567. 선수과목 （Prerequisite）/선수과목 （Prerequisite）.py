'''
바ㄴ례
4 3
1 2
2 3
1 3
2 다음 3 들을 수 있으므로 1 2 3 1 이 정답이래
조건으로 넣어줬으면 좋았을걸

바꿔야해
'''

import sys
from collections import deque

def bfs(dest):
    global lst, grp
    q = deque()
    q.append(dest)

    if grp[dest] == []:
        lst[dest] = 1

    while q:
        dest = q.popleft()
        for i in grp[dest]:
            lst[dest] = max(lst[dest], lst[i]+1)

n, m = map(int, sys.stdin.readline().split())
grp = {i:[] for i in range(1, n+1)}
lst = [0] * (n+1)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    grp[end].append(start)

for i in range(1, n+1):
    if lst[i] == 0:
        bfs(i)
    
print(*lst[1:])
# print(grp)