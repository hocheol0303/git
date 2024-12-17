'''
모든 지점에서 다른 모든 지점까지의 최단경로 << "모든"에서 다익스트라와 다름
갈 수 없거나 자기자신은 0으로 출력

플로이드 워셜 문제래 아직도 난 이게 뭔지 모르겠다

경유 - 출발 - 도착이었나

그래프 하나로 완결 내는거
grp에 정보 담았어
for mid ~:
    for start ~:
        for end ~:
            grp[start][end] = min(grp[start][end], grp[start][mid]+grp[mid][start])
원리는 잘 모르겠음 강의 같은거 봐야할듯
'''

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
grp = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    grp[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    grp[start-1][end-1] = min(cost, grp[start-1][end-1])

for mid in range(n):
    for start in range(n):
        for end in range(n):
            grp[start][end] = min(grp[start][end], grp[start][mid] + grp[mid][end])


for i in range(n):
    for j in range(n):
        if grp[i][j] == float('inf'):
            grp[i][j] = 0

for i in grp:
    print(*i)