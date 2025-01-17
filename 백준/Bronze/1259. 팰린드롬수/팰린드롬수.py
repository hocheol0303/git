import sys

while True:
    lst = list(sys.stdin.readline().rstrip())
    if lst[0] == '0':
        break

    check = True
    for i in range(len(lst) // 2):
        if lst[i] != lst[-i-1]:
            check = False
            break
    if check:
        print('yes')
    else:
        print('no')