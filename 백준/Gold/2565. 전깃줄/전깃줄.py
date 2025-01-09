'''
겹치지 않게하기 위해 없애야하는 전깃줄의 최소 개수
한 위치엔 하나의 전깃줄만 들어감

가장 많이 교차된거 지우기? -> ㄴㄴ 틀린 사례가 있음

컨닝: 가장 긴 증가하는 부분수열
어떻게 도출하지?: 예시 몇 개 직접 해보면 남는게 항상 가장 긴 증가하는 부분수열임을 알 수 있었대
1. a 기준으로 정렬 필요
2. b에서 가장 긴 증가하는 부분수열 추출
3. 답 = n-len(가장 긴 증가하는 부분수열)
'''
import sys

n = int(sys.stdin.readline())
lst = []
b = []
dp = [1]*(n+1)
max_ = 0

for _ in range(n):
    pos_a, pos_b = map(int, sys.stdin.readline().split())
    lst.append((pos_a, pos_b))

lst.sort(key = lambda x:x[0])
for val_a, val_b in lst:
    b.append(val_b)

for i in range(n):
    for j in range(i):
        if b[i] > b[j]:
            dp[i] = max(dp[j]+1, dp[i])
            max_ = max(max_, dp[i])

print(n-max_)