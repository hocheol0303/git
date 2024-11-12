'''
쫙 써놓고 규칙찾기 실패
뭔가 겹치는데 배수?? ㅁㄹ겠셔
배수가 되는거 다 버리고 나누어떨어지는 것만 추가 - 안됨
컨닝 슈웃
테이블 만들어놓고 갱신하는데, 뭔가.. 뭔가..
'''

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
lst = []

dp = [0]*(k+1)
dp[0] = 1

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

# lst.sort()

for i in range(n):
    for j in range(lst[i], k+1):
        dp[j] += dp[j-lst[i]]

print(dp[-1])
# print(lst)