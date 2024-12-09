'''
스택 쓰기
L: lst에서 stack으로 push
D: stack에서 lst로 push
B: lst pop
P: lst push
'''
import sys

lst = list(map(str, sys.stdin.readline().rstrip()))
stack = []

n = int(sys.stdin.readline())
for _ in range(n):
    inputs = list(map(str, sys.stdin.readline().split()))
    if len(inputs) == 2:
        symbol, string = inputs
    else:
        symbol = inputs[0]
    if symbol == 'L':
        if len(lst) > 0:
            stack.append(lst.pop())
    elif symbol == 'D':
        if len(stack) > 0:
            lst.append(stack.pop())
    elif symbol == 'B':
        if len(lst) > 0:
            lst.pop()
    elif symbol == 'P':
        lst.append(string)

while stack:
    lst.append(stack.pop())

print(''.join(lst))