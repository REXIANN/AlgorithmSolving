# 5642.py 합

import sys
sys.stdin = open("5642input.txt", "r")

tc = int(input())

for test_count in range(1, tc + 1):
    N_ = int(input())
    num_list = list(map(int, input().split()))
    sum_, sum_max = -1, -1

    for i in range(1, 1 << N_):
        for j in range(N_):
            for k in range(N_ - j):
                if i & (2 ** (j + 1) - 1):
                    sum_ += num_list[j]
        
        if sum_ > sum_max:
            sum_max = sum_ 
            print(i, j)
        sum_ = 0

    print('#{} {}'.format(test_count, sum_max))



