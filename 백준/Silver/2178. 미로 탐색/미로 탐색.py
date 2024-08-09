'''
DFS/BFS
행 n, 열 m 입력
1은 이동가능, 0은 불가능
(1,1)에서 출발하여 (n,m)으로 이동할 때 지나야 하는 최소 칸 수를 구하기

(1,1)도 1회취급

최소 칸 수를 구하려면 이전칸까지의 이동 칸 수 정보 필요
'''
import sys
from collections import deque

def bfs():
    global lst,n,m
    # 상하좌우 순 탐색
    row=0
    col=0
    d_row=[-1,1,0,0]
    d_col=[0,0,-1,1]
    q=deque()
    q.append([row,col])

    while q:
        row,col=q.popleft()

        # 큐에 삽입
        for i in range(4):
            tmp_row=row+d_row[i]
            tmp_col=col+d_col[i]

            # 인덱스 밖, 벽은 패스
            if tmp_row>=n or tmp_col>=m or tmp_row < 0 or tmp_col < 0 or lst[tmp_row][tmp_col] == 0:
                continue

            elif lst[tmp_row][tmp_col] == 1:
                q.append([tmp_row,tmp_col])
                lst[tmp_row][tmp_col] = lst[row][col]+1

            elif lst[tmp_row][tmp_col] > 1:
                if lst[tmp_row][tmp_col] > lst[row][col]+1:
                    lst[tmp_row][tmp_col] = lst[row][col]+1
        # breakpoint()


n,m=map(int, sys.stdin.readline().split())
lst =[]

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().rstrip())))
# print(lst)
bfs()
# print()
# for i in lst:
#     print(i)
print(lst[n-1][m-1])