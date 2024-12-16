'''
lst의 index = row
lst의 값 = col
'''

import sys

def find_avail(row, nums):
    global lst, n

    for r, c in enumerate(lst):
        nums[c] = False

        left = c - (row - r)
        right = c + (row - r)
        
        # print(f'{r}행 {c}열의 대각선 상 {row}행의 위치: {left}, {right}')
        if left >= 0:
            nums[left] = False
        if right < n:
            nums[right] = False
    
    # print(nums)

def dfs(depth):
    global lst, n, count
    nums = [True] * n

    if len(lst) == n:
        count += 1
        # print(lst)
    else:
        find_avail(depth, nums)
        for i in range(n):
            if nums[i] == True:
                lst.append(i)
                # print(lst)
                dfs(depth+1)
                lst.pop()

n = int(sys.stdin.readline())
lst = []
count = 0

dfs(0)
print(count)