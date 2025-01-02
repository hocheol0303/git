'''
4개의 톱니바퀴 나라배
톱니는 n극 or s극
왼쪽부터 1,2,3,4번
k번 회전시키려 함. 시계방향, 반시계방향
회전시킬 톱니바퀴, 방향 결정 필요

A 옆에 B 있다.
A를 회전시킬 때, 맞닿은 톱니의 극이 다르면 B는 A와 반대방향으로 회전함

회전시킬 때, 연쇄적으로 옆 톱니 회전시킬래? 아니면 밖에서 퍼져나갈래?

4줄에 톱니 상태 주어짐
12시부터 시계방향으로
1은 S극, 0은 N극
5줄에는 회전횟수
'''
import sys
from collections import deque

def func(num, direction):
    global cogwheels, check, dirs

    check[num] = 1
    dirs[num] = direction

    if num == 0:
        if check[num+1] == 0:
            if cogwheels[num][2] != cogwheels[num+1][6]:
                func(num+1, -direction)
            else:
                func(num+1, 0)
    if 1<=num<=2:
        if check[num+1] == 0:
            if cogwheels[num][2] != cogwheels[num+1][6]:
                func(num+1, -direction)
            else:
                func(num+1, 0)
        if check[num-1] == 0:
            if cogwheels[num][6] != cogwheels[num-1][2]:
                func(num-1, -direction)
            else:
                func(num-1, 0)
    if num == 3:
        if check[num-1] == 0:
            if cogwheels[num][6] != cogwheels[num-1][2]:
                func(num-1, -direction)
            else:
                func(num-1, 0)


def func2(num, dir): # dir을 보고 실제로 톱니바퀴 돌리는 시간~
    global cogwheels
    if dir == 1:
        # 시계
        cogwheels[num].appendleft(cogwheels[num].pop())
    elif dir == -1:
        # 반시계
        cogwheels[num].append(cogwheels[num].popleft())



score = 0
cogwheels = [deque() for i in range(4)]

for i in range(4):
    status = list(map(int, list(map(str, sys.stdin.readline().rstrip()))))
    cogwheels[i].extend(status)
    # print(status)

k = int(sys.stdin.readline())

for _ in range(k):
    check = [0]*4
    dirs = [0]*4 # 회전시킬 방향! 1 or -1
    num, direction = map(int, sys.stdin.readline().split())
    func(num-1, direction)
    for i in range(4):
        func2(i, dirs[i]) # i번 톱니바퀴를 돌려돌려 돌림판

for i in range(4):
    score += cogwheels[i][0]*(2**i)

# print(cogwheels)
print(score)