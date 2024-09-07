'''
마지막 지점 꼭 밟 -> 마지막 지점에서 출발

한 번에 1칸 or 2칸 ㄱㄴ
연속 3칸 안됨
ㅅㅂ

컨닝
dp == 밟아온 계단 발자취
각 계단마다 최적의 이전 발자취 골라 >>>> 3칸 고려하기 꽁짜
'''

import sys

n=int(sys.stdin.readline())
dp=[0]*(n+1)
steps=[0]*(n+1)

for i in range(1,n+1):
    steps[i]=int(sys.stdin.readline())

if n == 1:
    print(steps[1])
elif n==2:
    print(steps[1]+steps[2])
else:
    dp[1] = steps[1]
    dp[2] = steps[1]+steps[2]

    for i in range(3, n+1):
        dp[i]=max(dp[i-2]+steps[i], dp[i-3]+steps[i-1]+steps[i])    

    print(dp[-1])