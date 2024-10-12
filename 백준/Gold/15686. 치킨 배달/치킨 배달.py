'''
백트래킹
치킨집 없어지거나 아니거나니까 위치는 따로 저장해
시간초과 1: bfs 중간에 result가 min_보다 이미 크면 중단
시간초과 2: 컨닝 함 -> BFS가 없네
시간초과 3: calc_distance랑 dfs 더 줄여봄
    check 대신 now+1 넘겨주기로 중복 없는 탐색 ㄱㄴ
'''

import sys


# 백트래킹: dfs에서 걸러낸 lst, chicken_loc 잘 넘겨주면 됨?
def dfs(now):
    global n, m, chicken_loc, remain
    if len(remain) == m:
        calc_distance()
    else:
        for i in range(now, len(chicken_loc)):
            remain.append(chicken_loc[i])
            dfs(i+1)
            remain.pop()

def calc_distance():
    global min_, remain, house_loc
    result = 0
    for h_row, h_col in house_loc:    # 집집마다
        dist = float('inf')
        for c_row, c_col in remain: # 치킨집과의 거리 재고 최솟값 저장
            dist = min(dist, abs(c_row-h_row) + abs(c_col-h_col))
        result+=dist
        if result > min_:
            return
        
    min_ = min(min_, result)

n, m = map(int, sys.stdin.readline().split())
chicken_loc = []
house_loc = []

remain = []
min_ = float('inf')

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if lst[j] == 2:
            chicken_loc.append((i,j))            
        elif lst[j] == 1:
            house_loc.append((i, j))

dfs(0)
print(min_)