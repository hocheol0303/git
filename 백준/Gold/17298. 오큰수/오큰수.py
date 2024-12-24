'''
컨닝했음 엄청 생소해서 하루 지나면 까먹을듯
'''
import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
stack = [0]
ans = [-1] * n

for i in range(1, n):
    while True:
        if not stack or lst[stack[-1]] >= lst[i]:
            break
        if lst[stack[-1]] < lst[i]:
            ans[stack.pop()] = lst[i]
    stack.append(i)

print(*ans)