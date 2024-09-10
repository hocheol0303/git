'''
컨닝 딱 대
플로이드 워셜 : 그래프에서 가능한 모든 노드 쌍에 대해 최단거리를 구하는 알고리즘
    3중 for문으로 (출발지-도착지), (출발지-경유지)+(경유지-도착지) 중 최단거리를 비교하는 것
'''

import sys

n, m = map(int,sys.stdin.readline().split())

grp=[[float('inf') for j in range(n+1)] for i in range(n+1)]

for i in range(m):
    start, end = map(int , sys.stdin.readline().split())
    grp[start][end]=1

for i in range(1, n+1):         # 경유지
    for j in range(1, n+1):     # 출발지
        for k in range(1, n+1): # 도착지
            # 출발-도착 > 출발-경유 + 경유-도착 -> 업데이트
            if grp[j][k] > grp[j][i] + grp[i][k]:
                grp[j][k] = grp[j][i] + grp[i][k]

result = 0

for i in range(1, n+1):
    cnt=0
    for j in range(1, n+1):
        if grp[i][j] != float('inf') or grp[j][i] != float('inf'):
            cnt+=1

    if cnt == n-1:
        result+=1

print(result)