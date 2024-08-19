import sys
'''
n개 들ㅇㅓ와 m미터 필요해
'''
n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))

left = 0
right = lst[-1]

mid = 0
sum = 0
while left <= right:
    sum=0
    mid = (left + right) // 2
    for i in lst:
        if i>mid:
            sum += i-mid
    if sum == m:
        break
    elif sum < m:
        right = mid-1
    else:
        left = mid+1
    ####딱 맞게만 나와? 안나와


# 근사치에서 미세조정 피료행
if sum==m:
    print(mid)
elif sum<m:
    while sum<m:
        sum=0
        mid -= 1
        for i in lst:
            # 여기도 조건문 피료행
            if mid < i:
                sum+=i-mid
    print(mid)
else:
    while sum>m:
        sum=0
        mid += 1
        for i in lst:
            # 여기도 조건문 피료행2
            if mid<i:
                sum+= i-mid

    # 하드코딩 조져
    if sum < m:
        mid-=1
    print(mid)
    
#우웨에에에ㅔ에에에에에엑