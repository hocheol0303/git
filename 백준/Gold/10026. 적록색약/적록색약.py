import sys
from collections import deque

# 원래는 방문하면서 '.' 찍었으나 엄청 느림 -> 큐에 집어넣으면서 '.'찍기

def bfs(row,col):
    global lst,cnt
    q = deque()
    
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    
    q.append([row,col])
    check = lst[row][col]

    while q:
        row,col = q.popleft()
        lst[row][col]='.'

        for i in range(4):
            t_row = row+d_row[i]
            t_col = col+d_col[i]
            if t_row<0 or t_col<0 or t_row>=n or t_col>=n:
                continue
            elif lst[t_row][t_col] != check or lst[t_row][t_col] == '.':
                continue
            q.append([t_row,t_col])
            lst[t_row][t_col] = '.'
        # for i in lst:
        #     print(i)
        # print()
    cnt+=1

n = int(sys.stdin.readline())
lst=[]
tmp=[]
cnt=0
mapping = {'R':'R', 'G':'R', 'B':'B'}

for _ in range(n):
    input=list(map(str, sys.stdin.readline().rstrip()))
    lst.append(input)
    input=[mapping[x] for x in input]
    tmp.append(input)

# for i in lst:
#     print(i)

for i in range(n):
    for j in range(n):
        if lst[i][j] != '.':
            bfs(i,j)
print(cnt, end=' ')
lst = tmp
cnt=0
for i in range(n):
    for j in range(n):
        if lst[i][j] != '.':
            bfs(i,j)

# for i in tmp :
#     print(i)

# print(c_dict)
print(cnt)