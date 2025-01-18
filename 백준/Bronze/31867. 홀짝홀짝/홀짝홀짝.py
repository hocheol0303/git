import sys

n = int(sys.stdin.readline())
k = list(sys.stdin.readline().rstrip())
odd, even = 0, 0

for i in k:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

if odd == even:
    print(-1)
elif odd > even:
    print(1)
else:
    print(0)