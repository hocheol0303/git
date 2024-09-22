'''
a+b*c = abc*+
a*b+c = ab*c+
a*(b+c) = abc+*

우선순위 { +-, */, () }로 묶이는데 좀 이상했음

* 나왔는데 스택에 +: 쌓아
+ 나왔는데 스택에 *: 다 빼고 쌓아
( 보이면 )나올 때까지 따로 놀아 -> 재귀?

어케풀더라

'''

import sys

input_str = sys.stdin.readline().rstrip()
result=''
stack=[]

for i in input_str:
    if i.isalpha():
        result += i
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    elif not stack:
        stack.append(i)
    else:
        if i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(i)
        else:
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
while stack:
    result += stack.pop()
print(result)