'''
n으ㄴ 2부터
dp만으론 너무 오래걸림 n <= 1,000,000,000,000,000,000 미첬나 ?

규칙 찾음
a_{2n}=a_n(a_{n+1}+a_{n-1})\\
a_{2n+1}=a_n^2+a_{n+1}^2
이걸 재귀로 풀면 되는디

모듈러 연산 중간중간 넣을 수 있다. 그게 좋다.
'''

import sys

MOD = 1000000007

def fib(input):
    global dp, MOD          # dp용?

    if input in dp.keys():
        return dp[input]
    half = input // 2

    if input % 2 == 0:
        dp[input] = fib(half) * (fib(half+1) + fib(half-1)) % MOD
    else:
        dp[input] = (fib(half)**2 + fib(half+1)**2) % MOD
    
    return dp[input]


n = int(sys.stdin.readline())
dp = {0:0, 1:1, 2:1}
print(fib(n))