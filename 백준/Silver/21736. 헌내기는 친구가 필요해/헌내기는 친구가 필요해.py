import sys
from collections import deque

def bfs(lst, row, col):
    global n, m
    q=deque()
    q.append([row,col])
    d_row=[-1,1,0,0]
    d_col=[0,0,-1,1]

    count=0

    while q:
        row,col=q.popleft()

        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]

            if n_row<0 or n_col<0 or n_row>=n or n_col>=m:
                continue
            elif lst[n_row][n_col] == 'X' or lst[n_row][n_col] == '.':
                continue
            elif lst[n_row][n_col] == 'P':
                count+=1
                lst[n_row][n_col] = '.'
                q.append([n_row,n_col])        # 사람 만나고 방문
            elif lst[n_row][n_col] == 'O':
                q.append([n_row, n_col])
                lst[n_row][n_col]='.'

        # for i in lst:
        #     print(i)
        # print()

    if count:
        print(count)
    else:
        print('TT')


n, m = map(int, sys.stdin.readline().split())
lst=[]
for i in range(n):
    lst.append(list(map(str,sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(m):
        if lst[i][j] == 'I':
            bfs(lst,i,j)
            break