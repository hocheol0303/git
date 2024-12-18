'''
시간이 줄어들면서 출발위치로 돌아올 수 있으면 YES, 아니면 NO
    -> 음의 순환 확인하라?

벨만 포드: 다음을 v-1번 반복
    1. 모든 간선을 하나씩 확인한다.
    2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.

    v번 째 단계일 때에도 최단거리 테이블이 갱신된다면 음의 순환이 존재하는 것.

    for 정점 개수: 
        for 간선 개수:
    2중 반복문 사용함으로써 모든 정점에 대해 모든 간선을 한 번씩 보며 최단거리를 결정한 뒤, 마지막 v-1번째에서도 값이 갱신되면 음의 순환이 존재하는 것으로 판단함

    특징:
        edge를 하나의 리스트에 모아둠
        출발지점으로부터의 최단거리 확인을 위해 이중반복문을 사용하여 costs[start]가 ∞가 아닐 때(방문한 적 있을 때)에만 costs를 갱신할 기회가 주어짐 -> 여기서 2중 반복문 사용하는 이유 이해함
            >>>>>>>>>>>>>>>>> start에서 도달할 수 없는 음의 순환 있을 경우 못찾아냄 - 조건 빼


    왜 v-1번째에서 초기화가 일어나면 음의 순환인지 판단하는 이유 알면 벨만포드 끗
'''
import sys

def bellman_ford(start):
    global n, edges

    # float('inf')가 문제??
    costs = [10001] * (n+1)
    costs[start] = 0

    for i in range(n):
        for j in range(len(edges)):
            start, end, cost = edges[j]
            # if costs[start] != float('inf') and costs[end] > costs[start] + cost: >>> start에서 도달할 수 없는 음의 순환이 있을 수 있따.
            if costs[end] > costs[start] + cost:
                costs[end] = costs[start] + cost
                if i == n-1:
                    return True
        
    return False

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    edges = []

    # 걸리는 시간. 무방향 그래프
    for i in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    # 줄어드는 시간. 방향 그래프
    for i in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, -t))
    
    check = bellman_ford(1)
    if check:
        print('YES')
    else:
        print('NO')