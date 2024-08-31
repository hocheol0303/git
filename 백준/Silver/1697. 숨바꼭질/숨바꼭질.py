'''
가장 빠른 시간
선택지: +1 / -1 / *2
0 <= n,k <= 100,000
'''
import sys
from collections import deque

def bfs(x):
    global lst
    # dx = +1, -1, *2
    q = deque()
    q.append(x)

    while q:
        x=q.popleft()
        # if x >= 100000 or x < 0:
        #     continue
            
        if x < 100000:
            if lst[x+1]==0:
                q.append(x+1)
                lst[x+1]=lst[x]+1

        if x>0 and lst[x-1]==0:
            q.append(x-1)
            lst[x-1]=lst[x]+1
    
        if x!=0 and x*2<=100000 and lst[x*2]==0:
            q.append(x*2)
            lst[x*2]=lst[x]+1

n,k=map(int,sys.stdin.readline().split())
lst=[0]*100001

bfs(n)

# 시작점은 0이죠
lst[n]=0
print(lst[k])