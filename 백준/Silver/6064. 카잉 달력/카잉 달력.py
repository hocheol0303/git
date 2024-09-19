'''
m:n == 마지막 해

첫 해 = 1:1
둘째 해 = 2:2

x' = x+1 if x < m, else x' = 1
y' = y+1 if y < n, else y' = 1
'''

'''
1씩 더하는 코드는 시간초과
적절한 점화식이 필요해.?

컨닝합니다
m=10, n=12일 때
x=1, y=11 : count = 11 = m+1
x=3, y=1 : count = 13 = n+1
    => (count-x)%m==0 and (count-y)%n==0일 때 정답 -> 1부터 1씩 올리는거 시간초과
    얼마씩 올리야 정답될까 -> count=x부터 m씩 키우며 -> 어케나옴 : x,y를 모두 변수(=2변수)로 푸는 것보다 하나 고정하고 푸는게 낫다(=1변수). : count=x로 놓고 m씩 더하기 or count=y로 놓고 n씩 더하기 택1
'''

import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    m, n, x, y = map(int, sys.stdin.readline().split())
    cnt=y
    check=False
    while cnt <= m*n:
        if (cnt-x)%m == 0 and (cnt-y)%n == 0:
            check=True
            break
        else:
            cnt+=n
    if check:
        print(cnt)
    else:
        print(-1)