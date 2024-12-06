'''
빈: .
물: *
돌: X
굴: D
고: S
고슴도치, 물 동시 인접: 물이 먼저
S -> D
'''
import sys
from collections import deque

def bfs():
    global r, c, lst
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    q = deque()

    for row in range(r):
        for col in range(c):
            if lst[row][col] == 'S':
                lst[row][col] = now = 0
                q.append((row, col))
            if lst[row][col] == '*':
                q.append((row, col))
    
    while q:
        row, col = q.popleft()


        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0 <= n_row < r and 0 <= n_col < c:
                if lst[row][col] == '*':
                    if lst[n_row][n_col] == 'D' or lst[n_row][n_col] == 'X' or lst[n_row][n_col] == now or lst[n_row][n_col] == '*':
                        continue
                    else:
                        lst[n_row][n_col] = '*'
                        q.append((n_row, n_col))

                if type(lst[row][col]) == int:
                    if lst[n_row][n_col] == 'D':
                        # print('GOAL!!')
                        print(lst[row][col]+1)
                        return
                    elif lst[n_row][n_col] == 'X' or type(lst[n_row][n_col]) == int or lst[n_row][n_col] == '*':
                        continue
                    else:
                        lst[n_row][n_col] = lst[row][col] + 1
                        q.append((n_row, n_col))

        if type(lst[row][col]) == int:
            now += 1
        
        # print()
        # for i in lst:
        #     print(*i)


    print('KAKTUS')
        

r, c = map(int, sys.stdin.readline().split())
lst = []

for _ in range(r):
    lst.append(list(map(str, sys.stdin.readline().rstrip())))

# for i in lst:
#     print(*i)

bfs()