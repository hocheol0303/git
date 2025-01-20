import sys

N, S, R = map(int, sys.stdin.readline().split())
damaged = list(map(int, sys.stdin.readline().split()))
repair = list(map(int, sys.stdin.readline().split()))

lst = [0 if (i in repair and i in damaged) or (i not in repair and i not in damaged) else -1 if i in damaged else 1 for i in range(N+1)]

# print(lst)
for i in range(N+1):
    if i < N:
        if lst[i] == 1 and lst[i+1] == -1:
            lst[i] -= 1
            lst[i+1] += 1
        elif lst[i] == -1 and lst[i+1] == 1:
            lst[i] += 1
            lst[i+1] -= 1

print(lst.count(-1))