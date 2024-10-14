'''
3의 배수: 3나눠
2의 배수: 2나눠
1빼

1,000,000보다 작거나 같은 자연수가 1메가바이트??
메모리 512mb
'''

import sys
from collections import deque
import copy

x=int(sys.stdin.readline())

dp=[float('inf')]*(int(1e+6)+1)
q = deque()

dp[x]=0
dct={x:[x]}

q.append(x)

while dp[1] == float('inf'):
    x = q.popleft()
    if x % 3 == 0:
        if dp[x//3] > dp[x]+1:
            dp[x//3] = dp[x]+1
            q.append(x//3)
            if x // 3 in dct.keys():
                dct[x//3].append(x//3)
            else:
                dct[x//3] = copy.deepcopy(dct[x])
                dct[x//3].append(x//3)
    if x % 2 == 0:
        if dp[x//2] > dp[x]+1:
            dp[x//2] = dp[x]+1
            q.append(x//2)
            if x // 2 in dct.keys():
                dct[x//2].append(x//2)
            else:
                dct[x//2] = copy.deepcopy(dct[x])
                dct[x//2].append(x//2)
    if dp[x-1] > dp[x]+1:
        dp[x-1] = dp[x]+1
        if x-1 in dct.keys():
            dct[x-1].append(x-1)
        else:
            dct[x-1] = copy.deepcopy(dct[x])
            dct[x-1].append(x-1)
    if x-1 > 1:
        q.append(x-1)

print(dp[1])
print(*dct[1])