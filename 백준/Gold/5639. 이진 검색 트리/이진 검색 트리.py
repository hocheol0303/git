# 입력 크기 안정해줌 -> 컨닝: try로 함
# 런타임 에러: 10000개가 전부 한쪽으로 쏠리면 tree[10000]으로 안되지 안돼 -> 연결리스트로 풀어야함

import sys
sys.setrecursionlimit(10001)

class Node:
    def __init__(self, num):
        self.key = num
        self.left = None
        self.right = None

def insert(root, node):
    if node.key < root.key:
        if root.left:
            insert(root.left, node)
        else:
            root.left = node
    else:
        if root.right:
            insert(root.right, node)
        else:
            root.right = node

def postfix(root):
    if root.left:
        postfix(root.left)
    if root.right:
        postfix(root.right)
    print(root.key)


root = None
while True:
    try:
        num = int(sys.stdin.readline())
        node = Node(num)
        if not root:
            root = node
        else:
            insert(root, node)
    except:
        break

postfix(root)