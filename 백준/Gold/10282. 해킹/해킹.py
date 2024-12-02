'''
컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터 번호 c
d개 줄에 의존성을 나타내는 정수 a, b, s가 주어진다.
b 감염 시 s초 후 a도 감염

출력: 감염되는 컴퓨터 수, 시간
'''

import sys
import heapq

def func(start):
    global grp, times
    heap = []
    max_time = 0
    heapq.heappush(heap, (0, start))

    while heap:
        cost, start = heapq.heappop(heap)

        if times[start] == -1 or cost < times[start]:
            times[start] = cost
            for s, a in grp[start]:
                heapq.heappush(heap, (cost+s, a))
    
    print(len(times) - times.count(-1), max(times))


tc = int(sys.stdin.readline())
for _ in range(tc):
    n, d, c = map(int, sys.stdin.readline().split())
    grp = {i:[] for i in range(1, n+1)}
    times = [-1]*(n+1)

    for __ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        grp[b].append((s, a))
    
    func(c)
