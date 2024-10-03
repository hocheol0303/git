import sys
def dfs(start):
    global n, m, lst, output
    if len(output) == m:
        print(' '.join(map(str, output)))
    else:
        for i in range(0, n):
            if lst[i] in output:
                continue
            output.append(lst[i])
            dfs(i+1)
            output.pop()

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))
output = []

dfs(0)