'''
힙에는 양수만 넣고 음수양수 정보를 딕셔너리로 관리
'''

import heapq
import sys
n=int(sys.stdin.readline())
heap=[]
info={}

for _ in range(n):
    input_ = int(sys.stdin.readline())
    if input_ == 0:
        if len(heap) == 0:
            print(0)
            continue
        else:
            output=heapq.heappop(heap)
            if info[output]['-'] == 0:
                info[output]['+']-=1
                print(output)
            else:
                info[output]['-']-=1
                print(-output)

    else:
        abs_ = abs(input_)
        if abs_ not in info.keys():
            info[abs_]={'+':0, '-':0}
        
        heapq.heappush(heap, abs_)

        if input_ > 0:
            info[abs_]['+']+=1
        else:
            info[abs_]['-']+=1