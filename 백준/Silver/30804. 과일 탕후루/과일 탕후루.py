'''
n = 과일개수
lst = 꽂음
'''

import sys

n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))

front, rear = 0, 1
result=0
next_front=0

species=[lst[front]]

while rear<n:
    # 종이 하나일 때 새로운 종이 생기면 종 리스트에 추가
    if len(species) == 1 and lst[rear] not in species:
        species.append(lst[rear])
    # 아니면 여
    else:
        # 이미 2종 들고 있는데 새로운 종이 나왔어
        if lst[rear] not in species:
            # 지금까지의 최대 길이를 저장해놔
            result = max(result, rear-front)

            # next_front가 아닌거 (먼저 들어온거) 골라내ㅏㄹ
            for i in range(len(species)):
                if species[i] != lst[next_front]:
                    species.pop(i)
                    break
            
            species.append(lst[rear])
            front = next_front

    # next_front는 새로운 종의 첫 index
    if lst[rear-1] != lst[rear]:
        next_front=rear
    rear+=1

result=max(result, n-front)
print(result)