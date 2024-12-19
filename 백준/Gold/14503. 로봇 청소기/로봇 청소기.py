'''
현재칸 청소
주변 4칸 모두 청소: 후진, 후진 불가 시 작동 정지
청소되지 않은 칸: 청소된 칸 바라볼 때까지 반시계방향 90˚ 회전 후 전진

direction: 0, 1, 2, 3 == 북, 동, 남, 서
'''
import sys

n, m = map(int, sys.stdin.readline().split())
row, col, direction = map(int, sys.stdin.readline().split())
lst = []
count = 0
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

# 북 동 남 서 순으로
d_row = [-1,0,1,0]
d_col = [0,1,0,-1]

counterclockwise = [0,3,2,1]

while True:
    # 청소 했음을 2로 표시
    if lst[row][col] == 0:
        lst[row][col] = 2
        count += 1
    check = False
    # 주위 4칸에 청소할 곳 있는지 확인 후 전진
    for i in counterclockwise:
        i = (direction+i-1)%4
        n_row, n_col = row+d_row[i], col+d_col[i]
        if (0<=n_row<n and 0<=n_col<m) and lst[n_row][n_col] == 0:
            check = True
            direction = i # 방향 정하고
            row, col = n_row, n_col # 전진
            break

    if check:
        continue
    # 0인 바닥 못찾았을 때 후진
    else:
        # 후진 어떻게 할래
        # direction 보고
        i = (direction + 2) % 4
        n_row, n_col = row+d_row[i], col+d_col[i]
        if lst[n_row][n_col] == 1:
            break
        else:
            row, col = n_row, n_col

print(count)