import sys
from collections import deque

def bfs(idx, input, lst):
    q=deque()

    # list.index() 여러개
    for i, value in enumerate(input[idx]): 
        if value == 1:
            q.append(i)
            lst[idx][i]=1

    # lst[idx]에 방문표시 할거야
    while q:
        i=q.popleft()
        next=[j for j, value in enumerate(input[i]) if value==1 and lst[idx][j] == 0]

        for j in next:
            if lst[idx][j] == 0:
                q.append(j)
                lst[idx][j]=1


n = int(sys.stdin.readline())
input=[]
for i in range(n):
    input.append(list(map(int, sys.stdin.readline().split())))

lst=[[0]*n for i in range(n)]

for i in range(n):
    bfs(i, input, lst)

result=''
for i in range(n):
    for j in range(n):
        result+=str(lst[i][j])
        if j < n-1:
            result+=' '
    result+='\n'

print(result)