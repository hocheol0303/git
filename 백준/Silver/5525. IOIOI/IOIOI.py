'''
n: IOI의 'O' 개수
m: s의 길이
s: 문자열
'''

import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
s=sys.stdin.readline().rstrip()

p=list('IO'*n)
p.append('I')
p=''.join(p)

tmp=0
result=0
index=0
while True:
    if index != 0 and index == tmp:
        break
    else:
        tmp=index
    if p in s[index:]:
        index+=s[index:].index(p)+2
        result+=1
    else:
        break
print(result)

# result=0
# index=0
# while True:
#     if p in s:
#         index=s.index(p)+2
#         result+=1
#         s=s[index:]
#     else:
#         break
# print(result)