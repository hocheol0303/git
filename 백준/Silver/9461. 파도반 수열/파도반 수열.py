
import sys

tc=int(sys.stdin.readline())

for _ in range(tc):
    lst=[0,1,1,1,2,2,3,4,5,7,9]

    n=int(sys.stdin.readline())
    for i in range(11,n+1):
        lst.append(lst[i-1]+lst[i-5])

    print(lst[n])