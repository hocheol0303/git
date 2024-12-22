'''
퇴사일 이후에 끝나는건 못씀

dp 목적지부터 끝까지 덮어씌우는 방식: 시간초과 남
'''
import sys

n = int(sys.stdin.readline())
lst = [(0,0)]
dp = [0]*(n+1)

for i in range(n):
    term, pay = map(int, sys.stdin.readline().split())
    if i+term > n:
        lst.append((0,0))
    else:
        lst.append((term, pay))

for i in range(1, n+1):
    term, pay = lst[i]
    dp[i] = max(dp[i], dp[i-1])
    dp[i+term-1] = max(dp[i-1]+pay, dp[i+term-1])
    

# print(lst)
print(dp[-1])