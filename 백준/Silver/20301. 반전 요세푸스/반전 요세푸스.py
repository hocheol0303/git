'''
(N,K)-요세푸스 순열
N명이 원형으로 앉아있음
K번 사람 지우기 시작해서 그 사람의 오른쪽 K번째 사람 지움
모든 사람 제거되었을 때 제거된 사람의 순서

(7,3): [1,2,3,4,5,6,7]: 3,6,2,7,5,1,4


(N,K,M)-반전 요세푸스: M번 지울 때마다 반대 방향으로 돌림
(7,3,4)
[1,2,3,4,5,6,7]
3
[1,2,4,5,6,7]
6
[1,2,4,5,7]
2
[1,4,5,7]
7
[1,4,5]
1
[4,5]
5
[4]
4
'''

import sys

n,k,m = map(int,sys.stdin.readline().split())

lst = [i+1 for i in range(n)]
result=[]
# True == 우, False == 좌
direction=True
len_=n
loc=k-1
count=0

while lst:
    result.append(lst.pop(loc))
    len_-=1
    if len_==0:
        break
    count+=1
    if count == m:
        count = 0
        direction = not direction
    if direction:
        loc= (loc-1+k)%len_
    else:
        loc= (loc-k+len_)%len_

for i in result:
    print(i)