'''
길이가 n인 오르막 수
전판의 끝값 생각
이 아니라 전판의 첫값 생각
'''
import sys
n = int(sys.stdin.readline())
lst = [1]*10

for _ in range(n-1):
    for i in range(len(lst)):
        lst[i] = sum(lst[i:])

# print(lst)
print(sum(lst)%10007)