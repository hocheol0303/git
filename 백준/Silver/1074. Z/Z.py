'''
n, r, c 주면 2^n * 2^n map 위의 r행 c열의 z재귀 탐색 순서 출력
0부터 시작

규칙 찾다가 못 풂 
분할정복: 4개씩 계속 나눠간다는 힌트 컨닝

map을 4등분했을 때, 시작점을 빼면 전부 첫 번째 블록으로 끌어올 수 있어
어떻게 끌어와 : 0행 (2^n)//2열이 그놈임

n=3: 0~7
00=0
04=16
40=32
44=48

각 시작점 빼고 n-=1 : n=2
n=1까지 오면 맵에서 고르면 됨?
'''

import sys
n, r, c = map(int, sys.stdin.readline().split())

lst=[
    [0,1],
    [2,3]
]

def z(n, r, c):
    if n==1:
        return n, r, c, 0
    criteria = (2**n // 2)**2
    half = 2**n // 2
    pull = 0

    # # 4 7 7이 무한 루프 도는거 확인 -> n-1을 무조건 넘겨주기 위해 생각한 결과 이거 첫 번째 블록 조건이 위에 n==1 이랑 겹침
    # if r < half and c < half:
    #     return n, r, c, pull
    if r < half and c >= half:
        c -= half
        pull += criteria
    elif r >= half and c < half:
        r -= half
        pull += 2*criteria
    elif r >= half and c >= half:    # 내 논리상 else로 대체 가능 그냥 불안해여
        r -= half
        c -= half
        pull += 3*criteria
    
    return n-1, r, c, pull
    

pull=0
while True:
    n, r, c, tmp = z(n, r, c)
    pull += tmp
    if n == 1:
        break

print(lst[r][c]+pull)