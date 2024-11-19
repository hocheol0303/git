import sys
from collections import deque

def bfs():
    global lst, n
    q = deque()
    q.append((0,0))
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]
    record = [[float('inf')]*n for _ in range(n)]
    record[0][0] = lst[0][0]


    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row, n_col = row+d_row[i], col+d_col[i]
            if 0 <= n_row < n and 0 <= n_col < n:
                if record[row][col] + lst[n_row][n_col] < record[n_row][n_col]:
                    record[n_row][n_col] = record[row][col] + lst[n_row][n_col]
                    q.append((n_row, n_col))
    
    return record[-1][-1]

i = 0
while True:
    i+=1
    n = int(sys.stdin.readline())
    if n == 0:
        break
    lst=[]
    
    for _ in range(n):
        lst.append(list(map(int, sys.stdin.readline().split())))
    
    num = bfs()

    print(f"Problem {i}: {num}")