'''
root가 항상 1인가?
'''

import sys
from collections import deque

def func(target):
    global costs, prevs, available

    if available[target] == False:
        max_ = 0
        for p in prevs[target]:
            if available[p] == False:
                func(p)
            max_ = max(max_, costs[p] + costs[target])
        costs[target] = max_
        available[target] = True
    else:
        return

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    costs = [0]
    costs.extend(list(map(int, sys.stdin.readline().split())))

    nexts = [[] for __ in range(n+1)]
    prevs = [[] for __ in range(n+1)]
    
    # 입력 다 받은 후 available이 True인 놈은 종속성 없음
    available = [True]*(n+1) # 지었니 여부

    for __ in range(k):
        s, e = map(int, sys.stdin.readline().split())
        nexts[s].append(e)
        prevs[e].append(s)

        # e는 종속성이 생김
        available[e] = False
    
    target = int(sys.stdin.readline())

    # print(prevs)
    # print(costs)
    
    func(target)
    print(costs[target])