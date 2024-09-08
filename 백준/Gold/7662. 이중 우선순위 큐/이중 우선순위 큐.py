'''
첫 줄: TC
시작마다: 입력 개수
I n: n을 q에 삽입하는 연산
D 1: Q에서 최댓값을 삭제하는 연산
D -1: Q에서 최솟값을 삭제하는 연산

동기화 문제 못 풀었음 -> 딕셔너리로 해결하기 컨닝

틀: 출력 전에 max_ 꺼내고 nums[tmp] -= 1 추가
2틀: elif에 출력 추가
'''
import sys
import heapq

t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())
    min_heap=[]
    max_heap=[]
    cnt=0

    nums={}
    for __ in range(n):
        op, num = sys.stdin.readline().rstrip().split()
        num=int(num)

        if op == 'I':
            if num in nums:
                nums[num]+=1
            else:
                nums[num] = 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            cnt+=1
        else:
            if cnt==0:
                min_heap=[]
                max_heap=[]
                nums={}
                continue
            else:
                cnt-=1
                if num == 1:
                    tmp = -heapq.heappop(max_heap)
                    while True:
                        if nums[tmp] != 0:
                            nums[tmp] -= 1
                            break
                        else:
                            tmp = -heapq.heappop(max_heap)
                else:
                    tmp = heapq.heappop(min_heap)
                    while True:
                        if nums[tmp] != 0:
                            nums[tmp] -= 1
                            break
                        else:
                            tmp = heapq.heappop(min_heap)



    max_=None
    min_=None
    if cnt==0:
        print('EMPTY')
    elif cnt==1:
        while min_heap:
            tmp=heapq.heappop(min_heap)
            if nums[tmp] != 0:
                min_ = max_ = tmp
                break
        print(max_, min_)
    else:
        while max_heap:
            tmp=-heapq.heappop(max_heap)
            if nums[tmp] != 0:
                nums[tmp] -= 1
                max_=tmp
                break
        while min_heap:
            tmp=heapq.heappop(min_heap)
            if nums[tmp] != 0:
                min_=tmp
                break
        print(max_, min_)