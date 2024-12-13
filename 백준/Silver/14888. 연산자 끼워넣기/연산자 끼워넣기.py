'''
식의 계산은 연산자 우선순위를 무시하고 앞에서부터 진행
나눗셈은 정수 나눗셈으로 몫만 취함
음수를 양스로 나눌 때에는 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꿈

식의 결과의 최대/최소 구하기
'''

import sys

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a<0 and b>0:
        a = -a
        return -(a//b)
    else:
        return a//b

def dfs(lst):
    global min_ans, max_ans
    if len(lst) == len(ops):
        if tuple(lst) not in did:
            did.add(tuple(lst))
            # print(''.join(lst))
            
            ans = nums[0]
            for i in range(len(ops)):
                if lst[i] == '+':
                    ans = add(ans, nums[i+1])
                if lst[i] == '-':
                    ans = sub(ans, nums[i+1])
                if lst[i] == '*':
                    ans = mul(ans, nums[i+1])
                if lst[i] == '/':
                    ans = div(ans, nums[i+1])
            min_ans = min(min_ans, ans)
            max_ans = max(max_ans, ans)
    else:
        for i in range(len(ops)):
            if used[i] == 0:
                lst.append(ops[i])
                used[i] = 1
                dfs(lst)
                lst.pop()
                used[i] = 0

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
a, b, c, d = map(int, sys.stdin.readline().split())
min_ans = float('inf')
max_ans = -float('inf')
ops = []
lst = []
ops.extend(['+']*a)
ops.extend(['-']*b)
ops.extend(['*']*c)
ops.extend(['/']*d)
used = [0] * len(ops)
did = set()

# print(ops)
# print(-3//2) --- 뒤집어야함
dfs(lst)
print(max_ans)
print(min_ans)