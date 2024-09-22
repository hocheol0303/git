import sys
from collections import deque

'''
맨 뒤에 1 추가하거나 2를 곱하거나
'''

'''
탈출조건 때문에 계속 틀리는거 같은데,,,,,,,,,,,,,,,,,,,,,,
'''


def bfs(start, end):
    grp={}
    q = deque()

    time=1
    grp[start]=time
    q.append([start, time])

    while q and end not in grp.keys():
        start, time = q.popleft()
        
        if start > end:
            continue

        # 2 곱한거
        next_node1 = start*2

        # 1 붙인거
        next_node2 = start*10+1

        q.append([next_node1, time+1])
        q.append([next_node2, time+1])
        grp[next_node1] = time+1
        grp[next_node2] = time+1
    
    if end in grp.keys():
        print(grp[end])
    else:
        print(-1)


a,b=map(int, sys.stdin.readline().split())
bfs(a,b)