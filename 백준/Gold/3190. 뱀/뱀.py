'''
(0, 0)에서 오른쪽 보ㄴㅓ 시ㄱ
x초 후 c가 'L'이면 왼쪽, 'D'이면 오른쪽으로 90˚ 회전
시작 길이는 1

꼬리가 이전 꼬리의 위치를 가리키게 해
사과 먹을 때마다 list에 좌표 append하는식으로?
'''

import sys
from collections import deque

def turn(c, direction):
    if c == 'L':
        # 왼쪽
        direction = (direction - 1) % 4
    if c == 'D':
        # 오른쪽
        direction = (direction + 1) % 4
    
    return direction

# 나가면 끝, 꼬리 물면 끝
# 출발 하면서 1초: (0,1)을 채우고 1
# 3초에 D: 4초에 (1,3)자리
# 맵 밖으로 나갔어: 시간 세고 끝
def move(direction):
    # snake는 덱으로 바꿔야할듯
    global snake, n, lst
    # 북0 동1 남2 서3
    d_row = [-1,0,1,0]
    d_col = [0,1,0,-1]
    n_row, n_col = snake[0]
    
    n_row, n_col = n_row + d_row[direction], n_col + d_col[direction]
    if 0<=n_row<n and 0<=n_col<n:
        # 사과!!
        if lst[n_row][n_col] == 1:
            # 사과 묵고 꼬리 안잘라
            lst[n_row][n_col] = 0
            if (n_row, n_col) in snake:
                return -1
            else:
                snake.appendleft((n_row, n_col))
        elif lst[n_row][n_col] == 0:
            # 꼬리 먹었니 안먹었니
            if (n_row, n_col) in snake:
                return -1
            else:
                # 안먹었으면 끝꼬리 빼
                snake.pop()
                snake.appendleft((n_row, n_col))
    # 벽꿍
    else:
        return -1

    return 1

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
lst = [[0]*n for _ in range(n)]
direction = 1
count=0
# 북0 동1 남2 서3 로 둬
snake = deque()
snake.append((0,0))

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    lst[r-1][c-1] = 1

l = int(sys.stdin.readline())
act_list = []
for _ in range(l):
    x, c = map(str, sys.stdin.readline().rstrip().split())
    x = int(x)
    act_list.append((x, c))

# for i in lst:
#     print(i)
for x, c in act_list:
    while count < x:
        check = move(direction)
        count+=1

        if check == -1:
            print(count)
            exit()
    direction = turn(c, direction)


while check == 1:
    check = move(direction)
    count += 1

print(count)