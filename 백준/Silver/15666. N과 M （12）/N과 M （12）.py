import sys

def dfs(start):
    global n, m, lst, did
    if len(result) == m:
        if tuple(result) in did:
            pass
        else:
            print(*result)
            did.add(tuple(result))
    else:
        for i in range(start, n):
            result.append(lst[i])
            dfs(i)
            result.pop()


n, m = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))
result=[]
did=set()

dfs(0)