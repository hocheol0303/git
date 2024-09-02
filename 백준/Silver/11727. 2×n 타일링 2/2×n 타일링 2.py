'''
DP를 가장한 수학 구현
결과끼리 관계
'''

import sys
n=int(sys.stdin.readline())

lst=[0]*1001
lst[1]=1
lst[2]=3

for i in range(3,n+1):
    lst[i] = lst[i-2]*2+lst[i-1]

print(lst[n]%10007)