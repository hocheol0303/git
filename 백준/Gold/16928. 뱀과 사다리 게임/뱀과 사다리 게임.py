'''
게임 크기: 10x10
주사위 q : 1~6
i번에 있고 q가 나오면 i+q로 이동
주사위 결과가 100번 넘어가면 이동 불가
사다리는 숫자 커지게 이동
뱀은 숫자 작아지게 이동

사다리 수 n, 뱀의 수 m
n개 줄에 사다리 정보 (x번에 도착하면 y번으로 이동)
m개 줄에 뱀 정보 (u -> v)
1번, 100번은 뱀 x

1에서 100을 향한 최소 이동 횟수 출력
'''

'''
틀림: 뱀 / 사다리 만나면 거기에 머무를 수 있게 짰는데 아닌가봄 무조건 이동되는거 90 -> 1인 뱀 있을 때 90 밟으면 무조건 1인거
'''

import sys
from collections import deque

def bfs():
    global lst, times
    q = deque()
    q.append(1)
    times[1] = 0
    d_x = [1,2,3,4,5,6]

    while q:
        x = q.popleft()

        for i in range(6):
            n_x = x+d_x[i]

            if n_x > 100:
                continue
            if lst[n_x] == n_x and times[n_x] > times[x]+1:
                times[n_x] = times[x]+1
                q.append(n_x)
            elif lst[n_x] != n_x:
                if times[lst[n_x]] > times[x]+1:
                    times[lst[n_x]] = times[x]+1
                    q.append(lst[n_x])


n, m = map(int, sys.stdin.readline().split())

lst = [i for i in range(101)]
times = [float('inf')] * 101

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    lst[start] = end

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    lst[start] = end

bfs()
print(times[100])