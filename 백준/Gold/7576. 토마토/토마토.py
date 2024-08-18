import sys
from collections import deque

'''
베낌: 1이 여러개 있는 경우 동시에 탐색하는거 -> 1인 지점을 큐에 담아두고 함수에서 큐를 받아서 사용
'''

def bfs(lst, q):
    global cnt

    # row, col과 더해서 상하좌우 탐색할 때 더할 값
    d_row=[-1,1,0,0]
    d_col=[0,0,-1,1]

    while q:
        row, col = q.popleft()

        for i in range(4):
            n_row = row + d_row[i]
            n_col = col + d_col[i]
            
            if n_row < 0 or n_col < 0 or n_row >= r or n_col >= c:
                # out of range 피하기
                continue
            elif lst[n_row][n_col] == -1:
                # 벽 넘어가
                continue
            elif lst[n_row][n_col] == 0:
                # 방문안한 곳
                q.append([n_row, n_col])
                lst[n_row][n_col] = lst[row][col]+1
        # for i in lst:
        #     print(i)
        # print()
                


c, r = map(int,sys.stdin.readline().split())
cnt=0
lst=[]
q=deque()
for i in range(r):
    lst.append(list(map(int,sys.stdin.readline().split())))

# for i,j in zip(lst, count):
#     print(j)

for i in range(r):
    for j in range(c):
        if lst[i][j] == 1:
            q.append([i,j])

bfs(lst, q)

# bfs 돌았는데 0 있으면 -1 출력
check=1
for i in lst:
    if 0 in i:
        check=-1
        print(-1)
        break
    cnt = max(cnt, max(i))

if check==1:
    print(cnt-1) # 첫 번째 전염이 2부터 -> 원래 1부터