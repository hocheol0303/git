'''
갈 위치가 불이면 안됨
반례: @이 *보다 먼저 append 돼서 @ 움직이고 * 움직임 -> 시작점 넣을 때 *은 appendleft
    5 5
    ##.##
    #...#
    #.#.#
    #@#*#
    #####
'''

import sys
from collections import deque

def bfs(q):
    global lst, n, m
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]

    while q:
        row, col, symbol, count = q.popleft()
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0<=n_row<m and 0<=n_col<n:
                if symbol == '*' and (lst[n_row][n_col] != '#' and lst[n_row][n_col] != '*'):
                    lst[n_row][n_col] = '*'
                    q.append((n_row, n_col, '*', None))
                if symbol == '@' and lst[n_row][n_col] == '.':
                    if lst[n_row][n_col] == '*':
                        pass
                    else:
                        lst[n_row][n_col] = '@'
                        q.append((n_row, n_col, '@', count+1))
            if (not (0<=n_row<m and 0<=n_col<n)) and symbol == '@':
                return count
    
    return 'IMPOSSIBLE'

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    lst = []
    q = deque()

    for __ in range(m):
        lst.append(list(sys.stdin.readline().rstrip()))

    for r in range(m):
        for c in range(n):
            if lst[r][c] == '*':
                q.appendleft((r, c, '*', None))
            if lst[r][c] == '@':
                q.append((r, c, '@', 1))
    
    print(bfs(q))

    # print()
    # for i in lst:
    #     print(i)