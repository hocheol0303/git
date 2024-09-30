'''
백트래킹 첫 문제

1부터 n까지 중복 없는 m개의 수열

모르겠저
백츄래킹은 DFS 기반 재귀함수
'''

import sys

def dfs(start):
    global lst, m
    # 길이 맞으면 출력하고 나가
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    else:
        for i in range(start, n+1):
            if i not in lst:
                lst.append(i)
                dfs(i+1)
                lst.pop()

n, m = map(int, sys.stdin.readline().split())
lst = []

dfs(1)