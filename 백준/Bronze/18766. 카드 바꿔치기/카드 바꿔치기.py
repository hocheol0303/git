import sys

TC = int(sys.stdin.readline())
for _ in range(TC):
    n = int(sys.stdin.readline())
    before = list(map(str, sys.stdin.readline().split()))
    after = list(map(str, sys.stdin.readline().split()))

    check = False
    for i in before:
        if i in after:
            after.remove(i)
        else:
            check = True
    
    if check:
        print('CHEATER')
    else:
        print('NOT CHEATER')