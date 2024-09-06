'''
ㅁ
ㅣ
ㄱ
ㅗ
ㄹ
'''
# row, col 주면 거기서 시계로 돌리고 대칭하고 시계로 또돌려

def ㅁ(row, col):
    global n, m, lst, max_
    d_row = [0, 0, 1, 1]
    d_col = [0, 1, 0, 1]

    result=0
    for i in range(4):
        r = row+d_row[i]
        c = col+d_col[i]
        if r < 0 or c < 0 or r >= n or c >= m:
            result=0
            break
        result+=lst[r][c]

    max_ = max(max_, result)


def ㅣ(row, col):
    global n, m, lst, max_
    d_rows = [[0,0,0,0], [0,1,2,3]]
    d_cols = [[0,1,2,3], [0,0,0,0]]

    for tc in range(len(d_rows)):
        d_row = d_rows[tc]
        d_col = d_cols[tc]
        result=0
        
        for i in range(4):
            r = row+d_row[i]
            c = col+d_col[i]
            if r < 0 or c < 0 or r >= n or c >= m:
                result=0
                break
            result+=lst[r][c]

        max_ = max(max_, result)


def ㄱ(row, col):
    global n, m, lst, max_
    d_rows = [[0,0,0,1], [0,0,-1,-2], [0,1,1,1], [0,0,1,2],    [0,-1,-1,-1], [0,0,1,2], [0,0,0,-1], [0,1,2,2]]
    d_cols = [[0,1,2,2], [0,1,1,1],   [0,0,1,2], [0,-1,-1,-1], [0,0,1,2],    [0,1,1,1], [0,1,2,2],  [0,0,0,1]]

    for tc in range(len(d_rows)):
        d_row = d_rows[tc]
        d_col = d_cols[tc]
        result=0
        
        for i in range(4):
            r = row+d_row[i]
            c = col+d_col[i]
            if r < 0 or c < 0 or r >= n or c >= m:
                result=0
                break
            result+=lst[r][c]
            
        max_ = max(max_, result)


def ㅗ(row, col):
    global n, m, lst, max_
    d_rows = [[0,-1,0,0], [0,-1,0,1], [0,0,1,0],  [0,-1,1,0]]
    d_cols = [[0,0,1,-1], [0,0,1,0],  [0,1,0,-1], [0,0,0,-1]]

    for tc in range(len(d_rows)):
        d_row = d_rows[tc]
        d_col = d_cols[tc]
        result=0
        
        for i in range(4):
            r = row+d_row[i]
            c = col+d_col[i]
            if r < 0 or c < 0 or r >= n or c >= m:
                result=0
                break
            result+=lst[r][c]
            
        max_ = max(max_, result)

def ㄹ(row, col):
    global n, m, lst, max_
    d_rows = [[0,0,1,1], [0,1,1,2],   [0,0,1,1],    [0,1,1,2]]
    d_cols = [[0,1,1,2], [0,0,-1,-1], [0,-1,-1,-2], [0,0,1,1]]

    for tc in range(len(d_rows)):
        d_row = d_rows[tc]
        d_col = d_cols[tc]
        result=0
        
        for i in range(4):
            r = row+d_row[i]
            c = col+d_col[i]
            if r < 0 or c < 0 or r >= n or c >= m:
                result=0
                break
            result+=lst[r][c]
            
        max_ = max(max_, result)

import sys
n, m = map(int,sys.stdin.readline().split())
lst=[]
max_=0
for _ in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

for row in range(n):
    for col in range(m):
        ㅁ(row, col)
        ㅣ(row, col)
        ㄱ(row, col)
        ㅗ(row, col)
        ㄹ(row, col)

print(max_)