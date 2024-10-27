import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque()
count=0
lst=[]

for i in range(1, n+1):
    q.append(i)

while q:
    count+=1
    if count % k == 0:
        lst.append(q.popleft())
    else:
        q.append(q.popleft())

print('<'+', '.join(map(str, lst)), end='>')