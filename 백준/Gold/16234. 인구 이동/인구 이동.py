'''
인구 차이 L 이상, R 이하 -> 문 엶
문 다 열고 이동 시작
연합을 이루면 각 칸의 인구수는 {총 인구수} / {칸 개수}
소수점 버림

5//3 -> 버림

국경은 bfs로 열어?
'''

import sys
from collections import deque
from copy import deepcopy

def open_door(row, col, team_no):
    global lst, n, l, r, team, team_population, team_num
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    team_population.append(0)
    team_num.append(0)

    team[row][col] = team_no
    team_population[team_no] += lst[row][col]
    team_num[team_no] += 1
    q = deque([(row, col)])

    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0<=n_row<n and 0<=n_col<n:
                if team[n_row][n_col] == 0 and l <= abs(lst[row][col] - lst[n_row][n_col]) <= r:
                    team[n_row][n_col] = team_no
                    team_population[team_no] += lst[n_row][n_col]
                    team_num[team_no] += 1
                    q.append((n_row, n_col))

n, l, r = map(int, sys.stdin.readline().split())
lst = []
count = 0

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

before_lst = deepcopy(lst)

while True:
    team = [[0]*n for _ in range(n)]
    team_population = [-1]
    team_no = 1
    team_num = [-1]

    for row in range(n):
        for col in range(n):
            if team[row][col] == 0:
                open_door(row, col, team_no)
                team_no += 1
    
    # for i in lst:
    #     print(i)

    # print(team_population)
    # print(team_num)

    for row in range(n):
        for col in range(n):
            lst[row][col] = team_population[team[row][col]] // team_num[team[row][col]]

    if before_lst == lst:
        break
    else:
        before_lst = deepcopy(lst)
    count += 1

    # print()
    # for i in lst:
    #     print(i)

    # print(team_population)
    # print(team_num)
    # print()

print(count)