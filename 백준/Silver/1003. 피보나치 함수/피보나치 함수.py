import sys

# n = 0 ~ 40

n=int(sys.stdin.readline())

for i in range(n):
    zero=0
    one=0
    
    prepre_zero=1
    prepre_one=0

    pre_zero=0
    pre_one=1

    input = int(sys.stdin.readline())
    if input == 0:
        print(1,0)
    elif input==1:
        print(0,1)
    else:
        for j in range(input-1):
            zero=pre_zero+prepre_zero
            one=pre_one+prepre_one

            prepre_zero = pre_zero
            prepre_one = pre_one

            pre_zero=zero
            pre_one=one

        print(zero, one)