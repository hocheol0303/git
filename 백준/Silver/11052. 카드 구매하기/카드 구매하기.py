'''
n개가 포함된 카드팩
개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을거라고 믿는다.
카드가 i개 포함된 카드팩의 가격은 Pi원
지불해야하는금액의 최댓값

개당 가격을 생각해? x
개수당 최댓값으로 dp 만들어
    1개 살 때 최댓값, 2개 살 때 최댓값, ...
    아닌거 같아

dp의 인덱스를 뭐로 생각해야 활용할 수 있을까
    최대 묶음 개수?

n개 살 때 최댓값을 구해놓고 최대 n묶음일 때 최댓값을 구하기

미친 반례 벽 느껴지는데
12
1 1 6 8 11 1 1 1 1 1 1 1

컨닝
'''

import sys

n = int(sys.stdin.readline())
lst = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1)
# print(lst[1:])

for i in range(1, n+1):
    # i묶음 이하로만 묶을 수 있을 때 최댓값
    # dp[i] = lst[i] * (n//i) + lst[n%i]
    for j in range(1, i+1):
        dp[i] = max(dp[i], lst[j]+dp[i-j])

# print(lst)
# print(dp)

print(dp[-1])