'''
중복 숫자 있을 수 있음
봤던 수열은 또 나오지 않기 -> did에 저장
같은 인덱스의 수는 제외 -> check로 체크

did를 리스트로 놨을 때보다 set으로 놨을 때 훨씬 빨라짐
    8 8
    1 2 3 4 5 6 7 8
    로 확인
set은 리스트 안들어감 튜플 들어감
'''

import sys

def dfs():
    global lst, m, n, result, check
    if len(result) == m:
        if tuple(result) in did:
            pass
        else:
            print(*result)
            did.add(tuple(result[:]))
    else:
        for i in range(n):
            if check[i]:
                continue
            else:
                result.append(lst[i])
                check[i]=True
                dfs()
                check[i]=False
                result.pop()

n, m = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))
check = [False]*len(lst)
result = []
did = set()

dfs()