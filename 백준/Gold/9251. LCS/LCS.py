'''
아이디어 컨닝함: 2차원 DP행렬

위에꺼 따라가다가 같은글자 만나면 1 올리고 뒤로 쭉쭉 -> 점화식

ACAYKP
CAPCAK

  A C A Y K P
C 0 1 1 1 1 1
A 1 1 2 2 2 2
P 1 1 2 2 2 3
C 1 1 2 2 2 3
A 1 2 3 3 3 3
K 1 2 3 3 4 4

DP 테이블: 0 패딩 만들어쓰자
같은 문자열 나오면 dp[i-1][j-1] + 1
'''

import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# for i in dp:
#     print(i)

print(dp[-1][-1])