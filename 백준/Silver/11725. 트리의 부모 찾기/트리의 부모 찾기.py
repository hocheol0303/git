'''
순서 없는거 처리하는게 포인트
두 숫자 모두 등장한 적 없을 수 있음
    만들어져 있는 두 트리를 연결하는 일이 존재할 수 있따. == 누군가 연결되기 전까진 서로 누가 부모일지 모른다.

고집이 너무 쎄 틀린건 틀린거여
'''

import sys
from collections import deque

def bfs():
    global has_parent, dct
    q = deque()
    q.append(1)

    while q:
        start = q.popleft()

        for i in dct[start]:
            if has_parent[i] == -1:
                has_parent[i] = start
                q.append(i)

n = int(sys.stdin.readline())
dct = {i:[] for i in range(1, n+1)}
has_parent = [-1]*(n+1)

has_parent[1] = 1

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    dct[a].append(b)
    dct[b].append(a)

bfs()

# print(dct)
for i in has_parent[2:]:
    print(i)