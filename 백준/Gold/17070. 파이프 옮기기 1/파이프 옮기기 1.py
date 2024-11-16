import sys

def move_next(row, col):
    global lst, d

    for i in range(3):
        for n_row, n_col in d[i]:
            channel = None
            if [n_row, n_col] == [1, 0]:
                channel = 0
            elif [n_row, n_col] == [1, 1]:
                channel = 1
            elif [n_row, n_col] == [0, 1]:
                channel = 2
                
            if channel == 0:
                if (row+1 < n and col < n) and lst[row+1][col] == 1:
                    continue
            elif channel == 1:
                if ((row+1 < n and col < n) and lst[row+1][col] == 1) or ((row+1 < n and col+1 < n) and lst[row+1][col+1] == 1) or ((row < n and col+1 < n) and lst[row][col+1] == 1):
                    continue
            elif channel == 2:
                if (row < n and col+1 < n) and lst[row][col+1] == 1:
                    continue
            n_row += row
            n_col += col
            if n_row < n and n_col < n and lst[n_row][n_col] == 0:
                dp[n_row][n_col][channel] += dp[row][col][i]


n = int(sys.stdin.readline())
lst = []

# 전단계 어떻게 왔니~ 로 도착 가짓수
dp = []
for i in range(n):
    dp.append([])
    for j in range(n):
        dp[i].append([0,0,0])

# 전단계 ↓ ↘︎ → 순으로 갈 수 있는 다음 칸
d = [[[1,0], [1,1]],        # 0, 1번에 넣어야함
     [[1,0], [1,1], [0,1]], # 0, 1, 2번에 넣어야함
     [[1,1], [0,1]]]        # 1, 2번에 넣어야함

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))


dp[0][1][2] = 1

for r in range(n):
    for c in range(1, n):
        move_next(r, c)

# for i in dp:
#     print(i)

print(sum(dp[-1][-1]))