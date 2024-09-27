import sys
n = int(sys.stdin.readline())

lst=set()
dct={}

for _ in range(n):
    name, act = map(str, sys.stdin.readline().split())
    if act == 'enter':
        lst.add(name)
    else:
        lst.discard(name)

# print(lst)
# print(dct)

lst = list(lst)
lst.sort(reverse=True)
for i in lst:
    print(i)