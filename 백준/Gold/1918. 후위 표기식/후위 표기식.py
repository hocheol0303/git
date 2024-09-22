import sys

input_str = sys.stdin.readline().rstrip()
result=''
stack=[]

for i in input_str:
    if i.isalpha():
        result+=i
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            result+=stack.pop()
        stack.pop()
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result+=stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(i)

while stack:
    result += stack.pop()

print(result)