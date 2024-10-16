import sys

def dfs(start):
    global n, m, lst
    if len(lst) == m:
        print(*lst)
    else:
        for i in range(1, n+1):
            if i in lst:
                continue
            else:
                lst.append(i)
                dfs(i)
                lst.pop()

n, m = map(int, sys.stdin.readline().split())
lst = []

dfs(0)