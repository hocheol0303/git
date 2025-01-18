'''
반례 : 0 0 
    정답 0 0
    출력 -1
'''

import sys
# a = 합, b = 차
a, b = map(int, sys.stdin.readline().split())

if a < b:
    print(-1)
else:
    x = (a+b)/2
    y = (a-b)/2

    if 0<x%1<1 or 0<y%1<1 or x < 0 or y < 0:
        print(-1)
    else:
        print(int(max(x, y)), int(min(x, y)))