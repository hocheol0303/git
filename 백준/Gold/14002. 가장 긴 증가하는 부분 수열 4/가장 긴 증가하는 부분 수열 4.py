'''
길이 리스트, 이전단계 노드 리스트

끝 값(n = 1일 때) 문제

length 무작정 초기화하는 문제
7
4 5 6 7 1 2 3
여기서 1 2 3이 뜸
'''

import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
befores = [-1] * (n)
dp = [1] * (n)

length = 1
idx = 0
stack = []

for current in range(n):
    for before in range(current):
        if lst[before] < lst[current] and dp[current] < dp[before]+1:
            dp[current] = dp[before]+1
            befores[current] = before
            
            if length < dp[current]:
                length = dp[current]
                idx = current

# print(dp)
# print(befores)
# print(length, idx)

while befores[idx] != -1:
    stack.append(lst[idx])
    idx = befores[idx]
stack.append(lst[idx])

print(length)
print(*stack[::-1])