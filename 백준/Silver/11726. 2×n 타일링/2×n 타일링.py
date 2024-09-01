'''
순열 공식이 있나봄
lst[n] = lst[n-1]+lst[n-2]
이제 뭔지 배우러 가야지
'''

import sys
n = int(sys.stdin.readline())
lst=[0]*1001

lst[1]=1
lst[2]=2

for i in range(3, n+1):
    lst[i]=lst[i-1]+lst[i-2]

print(lst[n]%10007)