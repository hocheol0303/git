'''
총 f층, 현위치 s층, 목적지 g층
u버튼은 위로 u층, d버튼은 아래로 d층
적어도 몇 번 눌러야하는지 출력
불가능은 use the stairs 출력
'''
import sys
from collections import deque

def bfs(start):
    global f, g, u, d
    q = deque()
    q.append(start)

    while q and lst[g] == float('inf'):
        start = q.popleft()
        if start+u <= f and lst[start+u] == float('inf'):
            lst[start+u] = lst[start]+1
            q.append(start+u)
        if 0 < start-d and lst[start-d] == float('inf'):
            lst[start-d] = lst[start]+1
            q.append(start-d)
    
    return lst[g] if lst[g] != float('inf') else "use the stairs"


f, s, g, u, d = map(int, sys.stdin.readline().split())
lst = [float('inf')] * (f+1)
lst[s] = 0

print(bfs(s))