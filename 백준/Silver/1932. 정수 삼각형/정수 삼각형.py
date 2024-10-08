'''
DP
배열 1부터 시작
n층: 왼쪽은 +n-1, 오른쪽은 +n
'''

import sys

floor = int(sys.stdin.readline())
lst=[0]
dp=[0]*(floor*(floor+1)//2+1)

for i in range(floor):
    lst.extend(list(map(int, sys.stdin.readline().split())))

# i=1
# for cur in range(floor+1):
#     for j in range(cur):
#         print(lst[i+j], end=' ')
#     i+=cur
#     print()


# i = 각 층의 가장 첫 번째 수
# 이전 층의 수만을 고르는게 필요
i=2
prev_i=0
dp[1]=lst[1]
max_ = lst[1]
for cur in range(2, floor+1):
    # print('cur:',cur)
    for j in range(cur):
        # print(lst[i+j],end=' ')
        left = i+j-cur
        right = i+j-cur+1
        if left < prev_i:
            left = 0
        if right >= i:
            right = 0
        # print(lst[left], lst[right])
        dp[i+j] = lst[i+j]+max(dp[left], dp[right])
        max_ = max(max_, dp[i+j])
    prev_i=i

    i+=cur
#     print()

# print(lst)
# print(dp)
print(max_)