'''
SK, CY 게임
돌 n개
1~3개 가져가 ->>> 1 또는 3개
    ㅂㅅ추
마지막 돌 가져가는 사람 승
완벽하게 게임했을 때 이기는사람?
SK 선

k개일 때 이기는 사람 정해져있음

4 배수 아니야?

홀짝?
'''
import sys

n = int(sys.stdin.readline())
dp = [0] * 1001

# n=1, 2, 3일 때 선 잡는 놈이 이김
# 4개 남았을 때 가져가야하는 놈 져
dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = False

for i in range(5, n+1):
    if not dp[i-1] or not dp[i-3]:
        dp[i] = True
    else:
        dp[i] = False

if dp[n]:
    print('SK')
else:
    print('CY')