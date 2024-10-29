'''
베껴쓰: 끝나는 시간을 각 회의실의 정체성으로 둬
'''

import sys
import heapq

n = int(sys.stdin.readline())
lst=[]
heap=[]

for _ in range(n):
    lst.append(tuple(map(int, sys.stdin.readline().split())))

# 시작시간 순으로 정렬해
lst.sort()

# print(lst)
heap.append(lst.pop(0)[1])

for start, end in lst:
    if heap[0] > start:
        heapq.heappush(heap, end)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, end)

print(len(heap))