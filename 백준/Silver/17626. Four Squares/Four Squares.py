'''
다이나믹 프로그래밍 문제
퍼져나가면서 그자리에 적는거여



"넷, 혹은 그 이하"
최대로 놓고 min()으로 쭉쭉쭉
'''
import sys

n=int(sys.stdin.readline())

lst= [1 if ((i**0.5)*10)%10==0 else 4 for i in range(50001)]

lst[1]=1
lst[2]=2
lst[3]=3

for i in range(4, n+1):
    j=1
    while(j**2) <= i:
        lst[i] = min(lst[i], lst[i-j**2]+1)
        j+=1

print(lst[n])