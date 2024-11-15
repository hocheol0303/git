import sys

def dfs(start):
    global m, lst
    if len(lst) == m:
        print(*lst)
    else:
        for i in range(1, n+1):
            lst.append(i)
            dfs(i+1)
            lst.pop()

n, m = map(int, sys.stdin.readline().split())
lst = []

dfs(1)