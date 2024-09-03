'''
bfs
'''

import sys
from collections import deque

def bfs(row, col):
    global count, lst, numbers
    numbers.append(0)
    q = deque()
    d_row=[-1,1,0,0]
    d_col=[0,0,-1,1]
    q.append([row,col])
    numbers[count]+=1
    lst[row][col]=0


    while q:
        row, col = q.popleft()

        for i in range(4):
            t_row = row+d_row[i]
            t_col = col+d_col[i]
            if t_row < 0 or t_col < 0 or t_row >= n or t_col >= n:
                continue
            elif lst[t_row][t_col] == 0:
                continue
            else:
                lst[t_row][t_col] = 0
                q.append([t_row, t_col])
                numbers[count]+=1
    
    count+=1
                
    

n=int(sys.stdin.readline())

lst=[]
numbers=[]
count=0
for i in range(n):
    lst.append(list(map(int,list(sys.stdin.readline().rstrip()))))

for r in range(n):
    for c in range(n):
        if lst[r][c] == 1:
            bfs(r, c)

print(count)
for i in sorted(numbers):
    print(i)