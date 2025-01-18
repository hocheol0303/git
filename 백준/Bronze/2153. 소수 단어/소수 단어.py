import sys

def trans(al):
    if ord('A') <= ord(al) <= ord('Z'):
        return ord(al)-ord('A')+27
    else:
        return ord(al)-ord('a')+1

# 소수 판별
lst = [True]*(52*20+1)
# '편의상 1도 소수라고 하자'
# lst[1] = False
lst[0] = False
for i in range(2, 52*20+1):
    for j in range(2, 52*20+1):
        if i*j>52*20:
            break
        else:
            lst[i*j] = False

# for i in range(53):
#     print(f'{i}:{check[lst[i]]}')

words = list(sys.stdin.readline().rstrip())
sum_alpha = 0
for i in words:
    sum_alpha += trans(i)

if lst[sum_alpha] :
    print('It is a prime word.')
else:
    print('It is not a prime word.')