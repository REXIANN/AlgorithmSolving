# 1959. 두 개의 숫자열

import sys
sys.stdin = open("1959input.txt", "r")

# N개의 숫자로 구성된 숫자열 A_i(i = 1 ~ N)과
# M개의 숫자로 구성된 숫자열 B_j(j = 1 ~ M)가 있다.
# 서로 마주보는 숫자들을 곱한뒤 모두 더할때 최댓값을 구하여라.
# 단 N과 M은 3이상 20이하이다.

tc = int(input())

for test_count in range(tc):
    N_, M_ = tuple(map(int, input().split()))
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    sum_lists = 0
    max_result = 0

    if len(a_list) < len(b_list):
        shorter_list = a_list
        longer_list = b_list
    else:
        shorter_list = b_list
        longer_list = a_list

    # print(N_, M_)
    # print('A:', len(longer_list), ' B:', len(shorter_list))
    # print('longer list', longer_list)
    # print('shorter list', shorter_list)

    for i in range(len(longer_list) - len(shorter_list) + 1):
        for idx, short in enumerate(shorter_list):
            sum_lists += short * longer_list[i + idx]
        
        if sum_lists > max_result:
            max_result = sum_lists

        sum_lists = 0

    print('#{} {}'.format(test_count + 1, max_result))
        




    

