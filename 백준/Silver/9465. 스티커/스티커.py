import sys

'''
dp 지나가면서 행별로 max값 두 개씩 정해야함
'''

t = int(sys.stdin.readline())

for _ in range(t):
    max_=0
    n = int(sys.stdin.readline())
    lst=[]
    dp=[[0]*n for i in range(2)]
    lst.append(list(map(int, sys.stdin.readline().split())))
    lst.append(list(map(int, sys.stdin.readline().split())))
    
    if n == 1:
        print(max(lst[0][0], lst[1][0]))
    elif n == 2:
        print(max(lst[0][1]+lst[1][0], lst[0][0]+lst[1][1]))
    else:   
        dp[0][0] = lst[0][0]
        dp[1][0] = lst[1][0]

        dp[0][1] = lst[1][0] + lst[0][1]
        dp[1][1] = lst[0][0] + lst[1][1]
        
        # 각 행의 max 2개씩 : 0행 계산용, 1행 계산용
        max_list = [[dp[0][0],dp[0][1]],
                    [dp[1][0],dp[1][1]]]
        # 0행 계산 시: 0번과 3번 비교
        # 1행 계산 시: 1번과 2번 비교
        
        for i in range(2, n):
            dp[0][i] = lst[0][i] + max(max_list[0][0], max_list[1][0], max_list[1][1])
            dp[1][i] = lst[1][i] + max(max_list[0][0], max_list[0][1], max_list[1][0])

            max_list = [[max(max_list[0][0], max_list[0][1]), dp[0][i]], 
                        [max(max_list[1][0], max_list[1][1]), dp[1][i]]]

            max_ = max(dp[0][i], dp[1][i], max_)
        
        print(max_)
    # print()
    # for l in lst:
    #     print(l)
    # print()
    # for d in dp:
    #     print(d)
    # print()