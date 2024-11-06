# 그냥 리스트는 너무 크니까 연결리스트로 어디서 온게 짱인지 알기

import sys
from collections import deque

def bfs(start, end):
    global lst
    q = deque()
    q.append(start)
    lst[start][0] = 0

    while lst[end][0] == float('inf'):
        start = q.popleft()

        if start+1 <= 100000 and lst[start+1][0] > lst[start][0]+1:
            lst[start+1][0] = lst[start][0]+1
            lst[start+1][1] = start
            q.append(start+1)
        if start-1 >= 0 and lst[start-1][0] > lst[start][0]+1:
            lst[start-1][0] = lst[start][0]+1
            lst[start-1][1] = start
            q.append(start-1)
        if start*2 <= 100000 and lst[start*2][0] > lst[start][0]+1:
            lst[start*2][0] = lst[start][0]+1
            lst[start*2][1] = start
            q.append(start*2)

n, k = map(int, sys.stdin.readline().split())

lst = [[float('inf'), i] for i in range(100001)]

bfs(n, k)

print(lst[k][0])

stack = []

while lst[k][1] != k:
    stack.append(k)
    k = lst[k][1]

stack.append(k)
print(*stack[::-1])