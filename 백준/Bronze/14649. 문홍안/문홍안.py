'''
파 -> 빨 -> 초 -> 파

파랑 개수, 초록 개수, 빨강 개수의 비율 구하기

'''

import sys

p = int(sys.stdin.readline())
n = int(sys.stdin.readline())
lst = [0] * 101
secretaries = []
for _ in range(n):
    secretaries.append(list(map(str, sys.stdin.readline().split())))
    secretaries[-1][0] = int(secretaries[-1][0])

for num, direction in secretaries:
    if direction == 'R':
        for i in range(num+1, 101):
            lst[i] = lst[i] + 1
    else:
        for i in range(num-1, 0, -1):
            lst[i] = lst[i] + 1

for i in range(len(lst)):
    lst[i] = lst[i] % 3

# print(lst)
print(f'{p*lst[1:].count(0)/100:.2f}')
print(f'{p*lst[1:].count(1)/100:.2f}')
print(f'{p*lst[1:].count(2)/100:.2f}')