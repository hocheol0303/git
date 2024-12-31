'''
처음 크기 2
1초에 상하좌우로 이동 가능
나보다 큰 물고기 = 벽
작은 고기 = 지나가면서 먹을 수 o
같은 고기 = 지나갈 수 o

1. 먹을 수 있는 고기 없으면 끝
2. 먹을 수 있는 고기 1마리 = 먹으러 감
3. 먹을 수 있는 고기 1마리보다 많아 = 가까운(거리 = 칸 수)
4. 같은 거리 여러개 = 가장 위(r 최소), 가장 왼(c 최소) 순서대로

이동에 1초, 먹는 시간 0초, 먹으면 빈칸
자신의 크기와 같은 수의 물고기를 먹을 때마다 크기 1 증가
    ex) 레벨 2: 2마리 먹으면 레벨 3

몇 초 동안 먹니

3렙: 2마리 먹어야됨: sum(fishes[:4]) >= 2
4렙: 2+3마리 먹어야됨: sum(fishes[:5]) >= 5
5렙: 2+3+4마리 먹어야됨: sum(fishes[:6]) >= 9
6렙: 2+3+4+5마리 먹어야됨: sum(fishes) >= 14
'''

import sys
from collections import deque

# 먹이 한 번 먹기
def bfs():
    global lst, n, fishes, level, loc, count, exp
    visited = [[0]*n for _ in range(n)]
    
    q = deque([loc])
    visited[loc[0]][loc[1]] = 1
    foodList = []

    dRow = [-1,1,0,0]
    dCol = [0,0,-1,1]

    # 먹으러 갈 수 있는 먹이 위치 탐색
    while q:
        row, col = q.popleft()
        distance = visited[row][col]+1
        for i in range(4):
            nRow, nCol = row+dRow[i], col+dCol[i]
            if 0<=nRow<n and 0<=nCol<n and visited[nRow][nCol] == 0:
                if (lst[nRow][nCol] == 0 or lst[nRow][nCol] == level):
                    visited[nRow][nCol] = distance
                    q.append((nRow, nCol))
                if 1<=lst[nRow][nCol]<level:
                    visited[nRow][nCol] = distance
                    q.append((nRow, nCol))
                    foodList.append((nRow, nCol, distance-1))
    
    # for i in visited:
    #     print(i)
        
    # 거리순 정렬, row 작은거, col 작은거 순서대로 정렬
    foodList.sort(key=lambda x:(x[2], x[0], x[1]))
    # print(foodList)
    
    # 먹이 먹기
    # 9 자리 바꿔야됨
    # 같은 거리 여러개면 위에 먼저, 왼쪽 먼저
    if len(foodList) == 0:
        return False
    else:
        nRow, nCol, distance = foodList[0]
        lst[loc[0]][loc[1]] = 0
        lst[nRow][nCol] = 9
        loc = (nRow, nCol)
        count += distance
        exp -= 1

        if exp == 0:
            level += 1
            exp = level

        return True

                    

n = int(sys.stdin.readline())
lst = []
fishes = [0]*8
level = exp = 2
loc = None
count = 0

for r in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for c in range(len(row)):
        if 1 <= row[c] <= 6:
            fishes[row[c]] += 1
        if row[c] == 9:
            loc = (r,c)
    lst.append(row)

# print(fishes)
# print(loc)

while True:
    check = bfs()
    if check:
        continue
    else:
        break
print(count)