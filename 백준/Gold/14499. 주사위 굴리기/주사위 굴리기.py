'''
주사위 굴리면서 도착한 자리에 0 찍혀있으면 주사위 밑면의 수를 지도에, 아니면 자리에 쓰여 있는 수를 주사위에 복사
0이 아닌 경우엔 복사하고 0으로 만드네

n개의 줄에 지도에 쓰여있는 수가 북->남, 서->동 순서대로 주어짐
동1 서2 북3 남4

포인터 개념이랑 헷갈림: 3 입력됐을 때 front, back = down, up 이렇게 해야하는데(덮어쓰기) 포인터로 생각해서 up, down으로 저장함

x, y가 행, 열이었네
'''

import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())
lst = []
dice = [0]*6

def move(x, y, direction):
    global dice, lst, n, m
    up, down, left, right, front, back = dice
    
    d_row = [None, 0,0,-1,1]
    d_col = [None, 1,-1,0,0]

    n_y, n_x = y+d_col[direction], x+d_row[direction]
    if 0<=n_y<m and 0<=n_x<n:
        # 동1 서2 북3 남4
        if direction == 1:
            up, down, left, right = left, right, down, up
        elif direction == 2:
            up, down, left, right = right, left, up, down
        elif direction == 3:
            up, down, front, back = front, back, down, up
        elif direction == 4:
            up, down, front, back = back, front, up, down
        

        if lst[n_x][n_y] == 0:
            lst[n_x][n_y] = down
        else:
            down = lst[n_x][n_y]
            lst[n_x][n_y] = 0

        # 굴렸어
        dice = [up, down, left, right, front, back]
        print(up)

        return n_x, n_y
    else:
        # 밖으로 나가는거면 아무 행동 x
        return x, y

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))
    # print(lst[-1])

commands = list(map(int, sys.stdin.readline().split()))
# print(commands)

for command in commands:
    x, y = move(x, y, command)
    # print(dice)
    # for i in lst:
    #     print(i)