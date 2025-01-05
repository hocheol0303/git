'''
컨닝: 
해당 자리에서 끝까지 갈 수 있는 경우의 수 저장해서 중복되는 경로는 스킵할 수 있게하기
재귀함수의 리턴값을 활용해야함

풀어도 풀은게 아니야..
'''

import sys
sys.setrecursionlimit(10**6)

def dfs(row, col):
    global MAP, dp, n, m
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]

    if row == n-1 and col == m-1:
        return 1
    elif dp[row][col] != -1:
        # 방문한 적이 있는 경로면 해당 자리가 가지고 있는 경우의 수를 리턴함으로써 중복 계산 단축
        return dp[row][col]

    # visited 계념으로 -1은 탐색한 적 없는, 0은 경우의 수가 0
    dp[row][col] = 0

    for i in range(4):
        n_row, n_col = row+d_row[i], col+d_col[i]
        if 0<=n_row<n and 0<=n_col<m:
            if MAP[n_row][n_col] < MAP[row][col]:
                dp[row][col] += dfs(n_row, n_col)
    
    return dp[row][col]


n, m = map(int, sys.stdin.readline().split())
MAP = []
dp = [[-1]*m for _ in range(n)]

for _ in range(n):
    MAP.append(list(map(int, sys.stdin.readline().split())))

# for i in MAP:
#     print(i)

dfs(0,0)

# for i in dp:
#     print(i)

print(dp[0][0])