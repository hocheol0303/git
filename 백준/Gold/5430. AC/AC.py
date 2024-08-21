import sys

################################# 컨닝해보니 list 함수 지양해야함

def preprocess():
    global lst
    lst=lst.replace('[','')
    lst=lst.replace(']','') 
    lst=list(map(int, lst.split(',')))

t = int(sys.stdin.readline())

for _ in range(t):
    command = list(sys.stdin.readline().rstrip())
    length=int(sys.stdin.readline())
    lst=sys.stdin.readline().rstrip()
    
    if lst == '[]':
        if 'D' in command:
            print('error')
        else:
            print('[]')
        continue
    elif lst.count('D') > length:
        print('error')
        continue

    preprocess()

    direct = 1          ############################################ reverse는 좀 걸리긴 함
    front = 0
    rear = len(lst)
    check=1
    for i in command:
        if i == 'R':
            direct*=(-1)
        elif i == 'D':
            if direct == 1:
                front+=1
            else:
                rear -= 1
            if front>rear:
                check=-1

    if check==-1:
        print('error')
    else:
        if direct==-1:
            lst=lst[front:rear]
            lst.reverse()
            print(str(lst).replace(' ',''))
        else:
            print(str(lst[front:rear]).replace(' ', ''))
