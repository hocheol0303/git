'''
두 수를 곱한 뒤 최대공약수로 나누면 최소공배수
유클리드 호제법: 최대 공약수 구하는 방법
    두 수 A > B
    A % B = C -> B % C = D -> C % D = E -> ...(나머지가 0이 될 때까지) -> X % Y = Z = 0일 때, A * B // Y = 최소공배수

'''

import sys
a, b = map(int,sys.stdin.readline().split())
target=a*b

if a == 1 or b == 1:
    print(a*b)
else:
    a,b = max(a,b), min(a,b)

    while a % b != 0:
        # print(a,b)
        a, b = b, a%b

    print(target // b)