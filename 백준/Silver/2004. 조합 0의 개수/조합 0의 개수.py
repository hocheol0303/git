'''
nCr = n! / (n-r)!n!

컨닝: 2, 5의 개수 세기 : 2로 나눈 결과를 더하면서 0이 될 때까지 반복하면 2의 개수임
'''
import sys

n, r = map(int, sys.stdin.readline().split())


son_num_of_2 = 0
son_num_of_5 = 0

mom_num_of_2 = 0
mom_num_of_5 = 0


# 2의 개수를 어케 셀까 : 올라가면서 세?
n_tmp = n
while n_tmp != 0:
    n_tmp //= 2
    son_num_of_2 += n_tmp

n_tmp = n
while n_tmp != 0:
    n_tmp //= 5
    son_num_of_5 += n_tmp

r_tmp = r
while r_tmp != 0:
    r_tmp //= 2
    mom_num_of_2 += r_tmp

r_tmp = r
while r_tmp != 0:
    r_tmp //= 5
    mom_num_of_5 += r_tmp

nmr_tmp = n-r
while nmr_tmp != 0:
    nmr_tmp //= 2
    mom_num_of_2 += nmr_tmp

nmr_tmp = n-r
while nmr_tmp != 0:
    nmr_tmp //= 5
    mom_num_of_5 += nmr_tmp

print(min(son_num_of_2-mom_num_of_2, son_num_of_5-mom_num_of_5))