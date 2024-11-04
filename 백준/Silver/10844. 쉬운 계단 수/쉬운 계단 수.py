'''
각 단마다 0~9로 끝나는 수 개수 세기
전단계에서 본인 ±1들의 개수 합이 본인 개수
'''

import sys
n = int(sys.stdin.readline())
lst1 = [1]*10
lst1[0] = 0
lst2 = [0]*10

for _ in range(n-1):
    for i in range(10):
        if i == 0:
            lst2[i] = lst1[i+1]
        elif i == 9:
            lst2[i] = lst1[i-1]
        else:
            lst2[i] = lst1[i-1]+lst1[i+1]
        
    lst1, lst2 = lst2, lst1

# print(lst1, lst2)
print(sum(lst1)%1000000000)