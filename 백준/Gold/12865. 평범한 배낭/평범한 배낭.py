'''
컨닝: 2차원 DP
dp[i][j] = 최대 무게 i, j번째 아이템까지 살펴봤을 때의 최대 가치

1차원으로 짜면 새로운 아이템이 들어왔고 바로 담지 않았을 경우 이후에 들어온 아이템과의 조합이 현재 담은 아이템 조합보다 가치가 높을 경우 알아낼 수 없다.
들어올 아이템 n, 최대 무게 k일 때 n * k의 2차원 배열을 사용

담을 아이템의 인덱스를 i, 가방의 허용 용량(가정)이 j, 담을 물건의 무게를 weight, 가치를 value로 둘 때
    1. 들어온 아이템의 무게가 가정한 허용 용량 j보다 클 때: j < weight: dp[i][j] = dp[i-1][j]
    2. 1이 아닐 때: j >= weight: dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j])
'''

import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0]*(k+1)]

for i in range(1, n+1):
    dp.append([0]*(k+1))
    weight, value = map(int, sys.stdin.readline().split())
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j]) # 안넣었을 때의 무게와 들어온 무게 뺀 무게에서 새 아이템 넣었을 때의 무게 비교

print(dp[-1][-1])