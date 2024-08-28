'''
D: *2 %10000
S: n-1, 0->9999
L: appendleft(pop)
R: append(popleft)


컨닝했숴: 다이나믹 프로그래밍으로 탈출조건 visited[target] == 1인 반복문
L, R 4자리수 훼이크 개쉐이야
문자열 += 문제????제발요
'''
import sys
from collections import deque

def bfs(x, target):
    global visited, result, start
    # 방문한적 있으면 나가
    if visited[target] == 1:
        return
    q = deque()
    visited[x] = 1
    q.append(x)

    # target에 방문할 때까지 찾아가
    # 최소한의 명령어 나열
    while visited[target] == 0:
        x = q.popleft()
        tmp = result[x]+'D'
        calc=D(x)
        length=len(result[calc])
        if len(tmp) < length or length==0:
            # x가 0이면 제끼기
            if x == 0:
                pass
            else:
                if calc != start:
                    result[calc] = tmp  
                q.append(calc)
                visited[calc]=1
        
        tmp = result[x]+'S'
        calc=S(x)
        length=len(result[calc])
        if len(tmp) < length or length==0:
            if calc != start:
                result[calc] = tmp
            q.append(calc)
            visited[calc]=1
        
        tmp = result[x]+'L'
        calc=L(x)
        length=len(result[calc])
        if len(tmp) < length or length==0:
            if calc != start:
                result[calc] = tmp
            q.append(calc)
            visited[calc]=1
        
        tmp = result[x]+'R'
        calc=R(x)
        length=len(result[calc])
        if len(tmp) < length or length==0:
            if calc != start:
                result[calc] = tmp
            q.append(calc)
            visited[calc]=1
            
def D(x):
    return (x*2)%10000

def S(x):
    return 9999 if x==0 else x-1

# 앞에서 떼다가 뒤에 붙여: 4자리수 아니면 0 채워: 어디 채워 -> 앞에 채워
def L(x):
    x = list(str(x))
    if len(x) !=4:
        for i in range(4-len(x)):
            x.insert(0, '0')
    x.append(x.pop(0))
    result=''.join(x)
    
    return int(result)

# 뒤에서 떼다가 앞에 붙여: 4자리수 아니면 0 채워: 어디 채워 -> 앞에 채워
def R(x):
    x = list(str(x))
    if len(x) != 4:
        for i in range(4-len(x)):
            x.insert(0,'0')
    x.insert(0, x.pop())

    result=''.join(x)
    return int(result)

# print(R(407))
# print(L(407))
# print(D(4000), D(5000))
# print(S(1), S(2))

n = int(sys.stdin.readline())

# visited[target]이 1 될 때까지 반복문 돌릴거야 ==> bfs로 했솨

for _ in range(n):
    visited = [0] * 10001
    result = ['']*10001
    start,target=map(int,sys.stdin.readline().split())
    bfs(start, target)

    print(result[target])