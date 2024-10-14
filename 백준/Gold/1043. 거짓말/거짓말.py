'''
과장하고싶은데 몇몇 사람은 그 이야기의 진실을 안다.
진실을 아는 사람들 앞에선 과장 못함
어떤 사람이 어떤 파티에서는 진실을 듣고 또 다른 파티에서는 과장된 이야기를 들었을 때 거짓말쟁이 됨 -> 클러스터

첫 줄: 사람 수, 파티 수
둘째 줄: 진실을 아는 사람 수, 번호
셋째 줄~: 파티에 오는 사람 수, 번호

진실을 아는 사람 set을 하나 만들어
만난 집단 set의 리스트 만들어서 진실을 아는 사람, 알게된 사람을 산정해

집단 사이의 연결고리가 필요해
(1,2), (3,4), (2,3) 주면 합쳐져?

union-find 알고리즘이 있대: parent로 cluster 구분하는 알고리즘
코테책 그래프 마지막 부분에 있는거네 부모 찾기? 서로소 집합!!

union-find: 같은 클러스터 내의 가장 작은 요소를 루트로 두는 클러스터링
find_parent: 클러스터의 구분을 위한거 (너는 몇 번 클러스터)
union: 
'''

def find_parent(x):
    global parent

    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    global parent

    parent_x = find_parent(x)
    parent_y = find_parent(y)
    if parent_x != parent_y:
        parent[max(parent_x, parent_y)] = min(parent_x, parent_y)

import sys
n, m = map(int, sys.stdin.readline().split())
truth=None
clusters=[]

second_input = sys.stdin.readline().rstrip()
if len(second_input) == 1:
    for i in range(m):
        sys.stdin.readline()
    print(m)

else:
    truth = set(map(int, second_input[2:].split()))
    parties = []
    parent = list(range(n+1))
    for _ in range(m):
        lst = list(map(int, sys.stdin.readline().split()))
        party = lst[1:]
        parties.append(party)
        for i in range(1, len(party)):
            union(party[i-1], party[i])

    truth = set(find_parent(i) for i in truth)   # truth에 있는 사람들과 연결되면 걔도 truth

    for party in parties:
        check = True
        for i in party:
            if find_parent(i) in truth:
                check = False
                break
        if check:
            continue
        else:
            m-=1
    
    print(m)