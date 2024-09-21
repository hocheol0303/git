'''
블록 제거 2초
블록 설치 1초
최대 높이 256

최소시간 필요
2개 이상 -> 높은거
땅 고르게 만드는데 걸리는 시간, 높이 출력
'''

'''
모든 칸의 높이가 같아야함
lst에는 index에 해당하는 높이를 가진 칸의 수를 저장
따라서 sum(lst) = m*n

거리로 생각하나?: 한 칸 위로는 1의 시간 들고 b-=1, 한 칸 아래로는 2의 시간 들고 b+=1
어느 높이가 최소 시간일지 탐색 : 높이를 결정할 변수 놓기
'''

import sys

n, m, b = map(int, sys.stdin.readline().split())
lst=[0] * 257
min_ = 256
max_ = 0
results=[]

for _ in range(n):
    blocks = list(map(int, sys.stdin.readline().split()))
    for item in blocks:
        lst[item] += 1
        # 깔려 있는 블록의 최대 높이, 최소 높이 가지고있어
        if item > max_:
            max_ = item
        if item < min_:
            min_ = item

for target_height in range(min_, max_+1):
    # 아래 반복 끝났는데 num_of_required가 양수면 블록 부족한거
    num_of_required=-b
    time=0
    for now_height in range(min_, max_+1):
        if target_height == now_height:
            continue
        elif target_height > now_height:
            # 쌓는 차례
            num_of_required += (target_height - now_height) * lst[now_height]
            time += (target_height-now_height) * lst[now_height]
        else:
            # 깎을 차례
            num_of_required -= (now_height - target_height) * lst[now_height]
            time += (now_height - target_height) * lst[now_height] * 2
    if num_of_required > 0:
        continue
    else:
        results.append((time, target_height))
            

# print(lst)
# print(min_, max_)
results.sort(key = lambda x : (x[0], -x[1]))
print(results[0][0], results[0][1])