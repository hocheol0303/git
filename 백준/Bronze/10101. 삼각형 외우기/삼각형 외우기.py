import sys

lst=[]

lst.append(int(sys.stdin.readline()))
lst.append(int(sys.stdin.readline()))
lst.append(int(sys.stdin.readline()))

if lst.count(60) == 3:
    print("Equilateral")
elif sum(lst) != 180:
    print("Error")
else:
    check=-1
    for i in lst[:-1]:
        if lst.count(i) > 1:
            print('Isosceles')
            check=0
            break
    if check==-1:
        print('Scalene')