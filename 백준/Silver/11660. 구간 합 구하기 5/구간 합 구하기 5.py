'''
변수 범위 보라 시간초과가 날 수밖에 없다 (1초 - 1024*1024*100000)
DP(점화식)로 풀어야 한다 -> 어케했노;;
먼저 dp 테이블을 (0,0)에서 현위치까지의 합으로 채워
행렬 그림 그리면서 dp 테이블을 어떻게 활용할지 생각
컨닝 좋은 블로그: https://jominseoo.tistory.com/101
'''

import sys

n, m = map(int, sys.stdin.readline().split())
lst=[]
dp = [[0]*(n+1) for i in range(n+1)]
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + lst[i-1][j-1] - dp[i-1][j-1]

for _ in range(m):
    result=0
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

    result = dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]
    print(result)