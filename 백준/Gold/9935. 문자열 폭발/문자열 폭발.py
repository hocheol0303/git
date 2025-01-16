'''
컨닝: 오히려 너무 복잡하게 생각하지 않고 풀어봤다
'''

import sys

lst = list(sys.stdin.readline().rstrip())
target = list(sys.stdin.readline().rstrip())
stack = []

for i in range(len(lst)):
    if lst[i] in target:
        stack.append(lst[i])
        if ''.join(target) == ''.join(stack[-len(target):]):
            for _ in range(len(target)):
                stack.pop()
    else:
        stack.append(lst[i])

print(''.join(stack)) if stack else print('FRULA')