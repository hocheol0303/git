'''
n: IOI의 'O' 개수
m: s의 길이
s: 문자열
'''

import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
s=sys.stdin.readline().rstrip()

# 컨닝
p='IOI'
index=0
iters=0
result=0

# 뭔지 알겠는데 50점 짜리가 왜 50점짜린지 모르겠음 이게 더 빨라?
while index<(m-1):
    # IOI의 개수를 세
    # IOIOI로 쭊쭊쭈꾸ㅉ꾸쭊 이어져 있으면 맨 앞의 IO 제외해가면서 얼마나 연결되어 있는지 아세요
    # 그 개수가 n과 같으면 답 += 1
    if s[index:index+3] == p:
        index+=2
        iters+=1
        if iters==n:
            result+=1
            iters-=1
    else:
        index+=1
        iters=0
print(result)