import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
stack = []

latest = 0

for i in lst:
    stack.append(i)
    while True:
        if len(stack) != 0 and stack[-1] == latest+1:
            stack.pop()
            latest+=1
        else:
            break
    
if len(stack) == 0:
    print('Nice')
else:
    print('Sad')