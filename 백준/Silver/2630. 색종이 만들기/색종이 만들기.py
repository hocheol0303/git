'''
전체 종이가 모두 같은 색이 아니면 가로세로 반띵해서 4군데로 나눠 다시 탐색
끝까지 탐색하면 모든 색이 같은색인거로
'''

def func(row_start, row_end, col_start, col_end):
    global ones, zeros, lst
    notation=lst[row_start][col_start]

    #탈출조건: 원소 하나짜리 넘어왔을 때 값 올리고 탈출
    if row_start == row_end and col_start == col_end:
        if notation == 1:
            ones+=1
            return
        else:
            zeros+=1
            return
    
    # 다른거 적발되면 4개로 나눠서 재귀
    for r in range(row_start, row_end):
        for c in range(col_start, col_end):
            if lst[r][c] != notation:
                r = (row_start+row_end) // 2
                c = (col_start+col_end) // 2
                
                func(row_start, r, col_start, c)
                func(row_start, r, c, col_end)

                func(r, row_end, col_start, c)
                func(r, row_end, c, col_end)
                return
            
    # 적발 안됐으면 클-린 -> 값 올려
    if notation == 1:
        ones+=1
    else:
        zeros+=1


import sys

n=int(sys.stdin.readline())
lst=[]
ones=0
zeros=0
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

# for i in lst:
#     print(i)
row = col = n

check=lst[0][0]

row_start=col_start=0
row_end=col_end=n

func(row_start, row_end, col_start, col_end)

print(zeros)
print(ones)