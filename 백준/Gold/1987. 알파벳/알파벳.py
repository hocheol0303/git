import sys

# dfs 문제로 들어왔지만 bfs로 풀어보려했는데 리스트 관리를 못하겠음 백트래킹으로 전환

def dfs(row, col, count):
    global r, c, lst, record, max_, d_row, d_col
    max_ = max(max_, count)

    for i in range(4):
        n_row, n_col = row+d_row[i], col+d_col[i]
        if 0 <= n_row < r and 0 <= n_col < c and lst[n_row][n_col] not in record:
            record.add(lst[n_row][n_col])
            dfs(n_row, n_col, count+1)
            record.remove(lst[n_row][n_col])


r, c = map(int, sys.stdin.readline().split())
lst = []
record = set()
max_ = 1
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]


for _ in range(r):
    lst.append(list(map(str, sys.stdin.readline().rstrip())))

record.add(lst[0][0])
dfs(0, 0, 1)
record.remove(lst[0][0])

print(max_)