'''
n개의 정수로 이루어진 수열에서
원소의 합이 s인 부분수열의 개수

부분수열 중복 안받아?
5 -2
-1 -1 -1 -1 -1
에 대해서 1이 정답임? 함 해보자 아니네

5 0
0 0 0 0 0
정답: 31
이거 어케하냐
'''

def dfs(start):
    global n, s, hi, ans, check
    if s == sum(hi) and len(hi) != 0 :
       ans += 1 
    #    check.add(tuple(hi))
    #    print(*hi)
    # else: # else가 아니래!!~!@!!~$#ㄸ@!~#@~@!~~@#!~#@ 신세계
    for i in range(start, n):
        hi.append(lst[i])
        dfs(i+1)
        hi.pop()

import sys

n, s = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
hi = []
ans = 0
# check = set()

dfs(0)
print(ans)