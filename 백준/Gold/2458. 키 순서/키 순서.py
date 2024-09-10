'''
컨닝 딱 대
플로이드 워셜 : 그래프에서 가능한 모든 노드 쌍에 대해 최단거리를 구하는 알고리즘
    3중 for문으로 (출발지-도착지), (출발지-경유지)+(경유지-도착지) 중 최단거리를 비교하는 것
'''

import sys


def func(start):
    global grp
    n_start=0
    for i in grp[start]:
        if grp[start][i] != float('inf'):
            grp[i][start]=1




n, m = map(int,sys.stdin.readline().split())

grp=[[0 for j in range(n+1)] for i in range(n+1)]

for i in range(m):
    start, end = map(int , sys.stdin.readline().split())
    grp[start][end]=1

    
for middle in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if grp[start][middle] and grp[middle][end]:
                grp[start][end]=1


result = 0

# n행의 숫자 개수 + n열의 숫자 개수 == 관련된 노드 개수
for i in range(1, n+1):
    cnt=0
    for j in range(1, n+1):
        cnt+= grp[i][j] + grp[j][i]

    if cnt == n-1:
        result+=1

print(result)