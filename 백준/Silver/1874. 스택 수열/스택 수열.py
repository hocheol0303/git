import sys

n=int(sys.stdin.readline())

num_set=[n-i for i in range(n)]
stack=[]

result=[]
check=False

count=n

while True:
    if count==0:
        break
    # print(num_set, stack)
    input=int(sys.stdin.readline())
    if num_set:
        if input>num_set[-1]:
            while True:
                if num_set[-1] == input:
                    num_set.pop()
                    result.append('+')
                    result.append('-')
                    break
                stack.append(num_set.pop())
                result.append('+')
                
        elif input==num_set[-1]:
            num_set.pop()
            result.append('+')
            result.append('-')
            
        elif input<num_set[-1]:
            if input == stack[-1]:
                stack.pop()
                result.append('-')
            else:
                pass
    else:
        if input == stack[-1]:
            result.append('-')
            stack.pop()
        else:
            pass
    if not stack and not num_set:
        check = True
        break
    count-=1

if check:
    for i in result:
        print(i)
else:
    print('NO')