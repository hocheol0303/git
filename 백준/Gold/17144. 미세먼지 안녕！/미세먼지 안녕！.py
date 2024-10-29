'''
공청 항상 1열에 존재, 두 행 차지

1초
1. 미세먼지가 있는 모든 칸에서 확산
4방향
인접한 방향에 공청 있거나 칸이 없으면 그방향 확산 x
확산되는 양은 A_{r,c}//5
(r,c)에 남은 미세먼지의 양은 A_{r,c} - (A_{r,c}//5 * 확산된 방향 개수)

2.공청
공청 바람 나옴
위쪽은 반시계방향 순환, 아래쪽은 시계방향 순환
바람 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
공청에서 부는 바람은 미세먼지가 없는 바람이고, 공청으로 들어간 미세먼지는 모두 정화됨

t초 후 남아있는 미세먼지 양

r,c,t
'''
import sys
from collections import deque

def dust_spread():
    global r, c, lst
    q = deque()

    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]

    for i in range(r):
        for j in range(c):
            if not (lst[i][j] == 0 or lst[i][j] == -1): 
                q.append((i,j,lst[i][j]))
    
    while q:
        row, col, dust_amount = q.popleft()
        count = 0
        spread_amount = dust_amount // 5
        for i in range(4):
            n_row, n_col = row + d_row[i], col + d_col[i]
            if 0 <= n_row < r and 0 <= n_col < c and lst[n_row][n_col] != -1:
                count += 1
                lst[n_row][n_col] += spread_amount

        lst[row][col] -= spread_amount * count
                
def operate_purifier():
    # 위쪽은 반시계, 아래쪽은 시계
    global purifier_pos, r, c, lst

    # 위쪽: 상 - 우 - 하 - 좌 순으로 땡겨땡겨
    pur_r, pur_c = purifier_pos[0]
    row, col = pur_r, pur_c
    lst[row-1][0] = 0
    row -= 1
    while row > 0:
        lst[row][0] = lst[row-1][0]
        row -= 1
    lst[row][0] = 0
    while col < c-1:
        lst[0][col] = lst[0][col+1]
        col += 1
    lst[0][col] = 0
    while row < pur_r:
        lst[row][col] = lst[row+1][col]
        row += 1
    lst[row][col] = 0
    while col > pur_c:
        lst[row][col] = lst[row][col-1]
        col -= 1
    lst[row][col+1] = 0
    

    #아래쪽: 하 - 우 - 상 - 좌 순으로 땡겨땡겨
    pur_r, pur_col = purifier_pos[1]
    row, col = pur_r, pur_c
    lst[row+1][0] = 0
    row += 1
    while row < r-1:
        lst[row][0] = lst[row+1][0]
        row += 1
    lst[row][0] = 0
    while col < c-1:
        lst[row][col] = lst[row][col+1]
        col += 1
    lst[row][col] = 0
    while row > pur_r:
        lst[row][col] = lst[row-1][col]
        row -= 1
    lst[row][col] = 0
    while col > 0:
        lst[row][col] = lst[row][col-1]
        col -= 1
    lst[row][col+1] = 0

r, c, t = map(int, sys.stdin.readline().split())
lst = []

purifier_pos = None

for row in range(r):
    lst.append(list(map(int, sys.stdin.readline().split())))
    if purifier_pos == None and lst[-1][0] == -1:
        purifier_pos = ((row, 0), (row+1, 0))


for _ in range(t):
    dust_spread()
    operate_purifier()

ans = 0
# print()
for i in lst:
    # print(i)
    ans += sum(i)
print(ans+2)