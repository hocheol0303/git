'''
계단을 찾기 리스트 빙빙 돌리면 계단으로 시작하는 모양으로 고정됨 -> 계단으로 고정된 모양의 전, 전전이 온전한 직사각형의 변 2개
'''

import sys

num_corn=int(sys.stdin.readline())
num_count=[0]*7
lst=[]

for i in range(6):
    lst.append(tuple(map(int, sys.stdin.readline().split())))
    num_count[lst[-1][0]]+=1

while True:
    if lst[0][0] == lst[2][0] and lst[1][0] == lst[3][0]:
        break
    else:
        lst.append(lst.pop(0))



# print(lst)
result = (lst[-1][1] * lst[-2][1] - lst[1][1] * lst[2][1]) * num_corn
# print(lst[-1], lst[-2], lst[1], lst[2], num_corn)
print(result)