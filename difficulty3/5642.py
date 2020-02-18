# 5642.py 합

import sys
sys.stdin = open("5642input.txt", "r")

# 1 <= T <= 20
# 3 <= N_ <= 100,000
# |정수| <= 1000

tc = int(input())

for test_count in range(1, tc + 1):
    N_ = int(input())
    num_list = list(map(int, input().split()))
    sum_ = 0

    for i in range(N_ - 1):
        for j in range(i, N_):
            sum_ = sum_ + num_list[j]
            num_list.append(sum_)
        sum_ = 0

    print('#{} {}'.format(test_count, max(num_list)))





# for i in range(1, N_ + 1):
#         for j in range(N_ - i + 1):
#             for k in range(j, j + i):
#                 sum_ += num_list[k]
#             if sum_ > sum_max:
#                 sum_max = sum_
#                 print('sum_max changed: ', sum_max)
#             sum_ = 0