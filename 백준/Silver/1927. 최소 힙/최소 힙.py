'''
최소힙: 맨 뒤에 넣고 비교하면서 올라가
index = 트리 순서
'''

import sys
class min_heap:
    def __init__(self):
        self.heap=[0]
    def __str__(self):
        return str(self.heap)
    def __len__(self):
        return len(self.heap)
    def push(self, x):
        idx = len(self.heap)
        if idx == 1:
            self.heap.append(x)
            return
        else:
            self.heap.append(x)
            while self.heap[idx//2] > x:
                self.heap[idx] = self.heap[idx//2]   # 끌어내려 -> idx//2는 빈자린겨
                idx //= 2
                
                if idx == 1:
                    break
            self.heap[idx] = x

    def pop(self):
        if len(self.heap) == 1:
            return 0
        else:
            output = self.heap[1]
            parent = 1
            child = 2

            if len(self.heap) == 2:
                return self.heap.pop()
            while child <= len(self.heap)-1:
                if child + 2 < len(self.heap):         # 0 인덱스에 안쓰는 값 넣어놔서 len = heap에 들어있는 값 + 1. 끝 인덱스에서 child+1 하려면 child가 len보다 2이상 작아야함
                    if self.heap[child] > self.heap[child+1]:
                        child += 1
                if self.heap[len(self.heap)-1] <= self.heap[child]:
                    break
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                parent = child
                child *= 2
            self.heap[parent] = self.heap.pop()

            return output


n = int(sys.stdin.readline())

heap=min_heap()

for i in range(n):
    input = int(sys.stdin.readline())
    if input == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(heap.pop())
    else:
        heap.push(input)
    # print(heap)