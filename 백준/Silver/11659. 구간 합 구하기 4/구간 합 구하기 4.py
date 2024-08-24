'''
컨닝: 수열의 합끼리 빼기: 2번부터 10번 합 = s(10) - s(2)
'''

import sys

n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))
lst_sum = [0]

for i in range(1, n+1):
    lst_sum.append(lst[i-1] + lst_sum[i-1])


for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(lst_sum[j]-lst_sum[i-1])      #### i가 1인 경우엔 j번째 값에서 0을 빼야 다 더한거