'''
그래프?
'''
import sys
from collections import deque

def add_graph(start, end, graph):
    # global graph
    if start not in graph.keys():
        graph[start]=[end]
    else:
        graph[start].append(end)

def bfs(s, graph):
    global n
    # start에서 각 점까지 최단거리
    cnt=[5000 for i in range(n+1)]
    start=s
    q=deque()
    for i in graph[start]:
        cnt[i]=1
        q.append(i)

    while q:
        start=q.popleft()
        iter=cnt[start]+1
        for i in graph[start]:
            if i==s or cnt[i] != 5000:          # 5000: bfs에서 방문을 일단 했으면 그게 최단거리야?
                continue
            elif cnt[i] > iter:
                cnt[i]=iter
            q.append(i)
    return sum(cnt)-5000*2

n, m = map(int, sys.stdin.readline().split())
graph={}
cnt_list=[]
min_val=5000
idx=-1

for _ in range(m):
    start, end = map(int,sys.stdin.readline().split())
    add_graph(start, end, graph)
    add_graph(end, start, graph)

for i in range(1,n+1):
    tmp=bfs(i, graph)
    cnt_list.append(tmp)
    if tmp < min_val:
        idx=i
        min_val=tmp

# print(cnt_list)
print(idx)