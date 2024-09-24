import sys

from collections import deque

def bfs():
    global start, end
    q = deque()

    lst=[float('inf')]*100001
    q.append(start)
    lst[start]=0

    while q:
        start = q.popleft()

        if start*2 <= 100000:
            if lst[start] < lst[start*2]:
                lst[start*2] = lst[start]
                q.append(start*2)
        if start+1 <= 100000:
            if lst[start]+1 < lst[start+1]:
                lst[start+1] = lst[start]+1
                q.append(start+1)
        if start-1 >= 0:
            if lst[start]+1 < lst[start-1]:
                lst[start-1] =lst[start]+1
                q.append(start-1)
    print(lst[end])

start, end = map(int, sys.stdin.readline().split())

bfs()