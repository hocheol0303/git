'''
오름차순인데 같은거 출력도 포함
'''

import sys

def dfs(idx):
    global ans, m, n, lst
    if len(ans) == m:
        print(*ans)
    else:
        for i in range(idx, n):
            ans.append(lst[i])
            dfs(i)
            ans.pop()

n, m = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))
ans = []

dfs(0)