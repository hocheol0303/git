import sys
from collections import deque

def bfs():
    global lst, q, c, r, h, count

    d_height=[-1,1,0,0,0,0]
    d_row=[0,0,-1,1,0,0]
    d_col=[0,0,0,0,-1,1]

    while q:
        height,row,col = q.popleft()
        for i in range(6):
            n_height= height+d_height[i]
            n_row= row+d_row[i]
            n_col= col+d_col[i]

            if n_height < 0 or n_row < 0 or n_col < 0 or n_height >= h or n_row >= r or n_col >= c:     # 범위 넘어가면 패스
                continue
            elif lst[n_height][n_row][n_col] == -1:     # 벽 패스
                continue
            elif lst[n_height][n_row][n_col] == 0:
                q.append([n_height,n_row,n_col])
                lst[n_height][n_row][n_col] = lst[height][row][col] + 1
                count = max(count, lst[height][row][col]+1)
        
        # for i in lst:
        #     print('------------------')
        #     for j in i:
        #         print(j)
        # print()
            
'''
col, row, height 순 입력
'''
c, r, h = map(int, sys.stdin.readline().split())
lst=[]
q= deque()
count=0
check = False

for i in range(h):
    tmp=[]
    for j in range(r):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        if 0 in tmp[j]:
            check=True
    lst.append(tmp)

# print(lst)
# for i in lst:
#     print(i)

if check:
    for i in range(h):
        for j in range(r):
            for k in range(c):
                if lst[i][j][k] == 1:
                    q.append([i,j,k])
    bfs()

    for i in range(h):
        for j in range(r):
            for k in range(c):
                if lst[i][j][k] == 0:
                    check=False
    if check:
        print(count-1)
    else:
        print(-1)
else:
    print(0)