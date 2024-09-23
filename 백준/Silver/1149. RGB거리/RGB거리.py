import sys
n = int(sys.stdin.readline())
lst=[]
dp=[[float('inf')]*3 for _ in range(n)]
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

# print(lst)
# dp[0][0]=1
# print(dp)

dp[0] = lst[0]

for i in range(1,n):
    lst[i], dp[i]
    dp[i][0] = lst[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = lst[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = lst[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))