'''
최소한의 연산으로 1 만들기

1. 3나눠지면 3나눠
2. 2나눠지면 2나눠
3. 1빼

DP

3으로 나눠지면 3 나누는게 제일 적고 그다음 2 나누기, 그다음 1 빼기 이렇게 가정하고 풀었다. >>> 맞음????? 아님아님 >>> 들고 있는 값 //3, //2, -1에 대한 횟수를 비교해서 최소인 놈 찾아가기
'''

import sys

lst=[0, 1]   # 지금 들고있는 값의 다음값을 뭐로 할지 정함 > 다 하고 나니 사용하진 않음. 디버깅할 때 봄
cnt=[0, 0]

n= int(sys.stdin.readline())
i=2



# 이전 값이 누가 더 작냐 비교
while i <= n:
    # cnt[i//3] vs cnt[i//2] vs cnt[i-1] 겨뤄보자
    tmp=cnt[i-1]
    index='-1'
    if i % 3 == 0:
        if tmp > cnt[i//3]:
            tmp = cnt[i//3]
            index='//3'
    if i % 2 == 0:              #elif를 왜 넣니이이이이
        if tmp > cnt[i//2]:
            tmp = cnt[i//2]
            index='//2'
    
    if index == '//3':
        lst.append(i//3)
        cnt.append(cnt[i//3]+1)
    elif index == '//2':
        lst.append(i//2)
        cnt.append(cnt[i//2]+1)
    else:
        lst.append(i-1)
        cnt.append(cnt[i-1]+1)

    i+=1


print(cnt[n])