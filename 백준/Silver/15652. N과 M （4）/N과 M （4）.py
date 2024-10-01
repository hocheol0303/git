import sys

def dfs(start):
    global lst, m
    if len(lst) == m:
        print(' '.join(map(str, lst)))
    else:
        for i in range(start, n+1):
            lst.append(i)
            dfs(i)
            lst.pop()

n, m = map(int, sys.stdin.readline().split())
lst = []

dfs(1)