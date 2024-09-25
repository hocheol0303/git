import sys
n=int(sys.stdin.readline())

# 이전 단계의 값들 저장하는거
dp_max=[0,0,0]
dp_min=[0,0,0]
min_ = max_ = None

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if i == 0:
        dp_max=[a,b,c]
        dp_min=[a,b,c]
    else:
        new_max_a = a + max(dp_max[0], dp_max[1])
        new_max_b = b + max(dp_max[0], dp_max[1], dp_max[2])
        new_max_c = c + max(dp_max[1], dp_max[2])
        dp_max = [new_max_a, new_max_b, new_max_c]

        new_min_a = a + min(dp_min[0], dp_min[1])
        new_min_b = b + min(dp_min[0], dp_min[1], dp_min[2])
        new_min_c = c + min(dp_min[1], dp_min[2])
        dp_min = [new_min_a, new_min_b, new_min_c]

print(max(dp_max), min(dp_min))