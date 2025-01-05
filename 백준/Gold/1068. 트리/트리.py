'''
다중 자식이 가능하다!!! 이 문젠가?
'''

import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

def count_leaf(node_num):
    global delete_target, nodes
    leaves = 0
    node = nodes[node_num]
    if len(node.children) == 0:
        return 1
    else:
        for child in node.children:
            leaves += count_leaf(child)
        return leaves

n = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))
delete_target = int(sys.stdin.readline())
root = None

if inputs[delete_target] == -1:
    print(0)
else:
    nodes = [None] * n
    for i in range(n):
        nodes[i] = Node(i)

    for i in range(n):
        if inputs[i] == -1:
            root = i
        else:
            nodes[inputs[i]].children.append(i)


    target_parent = nodes[inputs[delete_target]]
    target_parent.children.pop(target_parent.children.index(delete_target))

    print(count_leaf(root))