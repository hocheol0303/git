import sys
# import time

n = int(sys.stdin.readline())
# start = time.time()
# 1로 이루어진거로 초기화
# 제곱수를 저장해보까?

dp = [i for i in range(n+1)]
squared_nums = [4]

num = 2

for i in range(4, n+1):
    if i == (num+1)**2:
        num += 1
        squared_nums.append(num**2)
        dp[i] = 1
    else:
        for j in squared_nums:
            if i - j == 0:
                dp[i] = 1
            else:
                dp[i] = min(dp[i], 1+dp[i-j])

print(dp[n])
# end = time.time()
# print(round(end-start, 2))