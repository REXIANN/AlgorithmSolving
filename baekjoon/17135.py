# 17135.py 캐슬디펜스
from pprint import pprint
import copy
import sys
sys.stdin = open("17135input.txt", "r")


tc = int(input())
for test_count in range(1, tc + 1):
    N, M, D = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    count_list = []
    final_list = []
    flag = 0
    row, col = N-1, -1
    for i in range(M - 2):
        for j in range(i + 1, M - 1):
            for k in range(j + 1, M):
                trial_list = [i, j, k]
                copy_mat = copy.deepcopy(matrix)
                for l in range(N -1, -1, -1):
                    for asdf in trial_list:
                        for m in range(1, 2 * D, 2):
                            for n in range(-(m // 2), m // 2 + 1, 1):
                                row_in, col_in = (l - (m // 2 - abs(n))), (asdf + n)
                                if 0 <= row_in < N and 0 <= col_in < M and copy_mat[row_in][col_in] >= 1:
                                    copy_mat[row_in][col_in] += 1
                                    flag = 1
                                    break
                            if flag:
                                flag = 0
                                break

                    for x in range(N):
                        for y in range(M):
                            if copy_mat[x][y] > 1:
                                count += 1
                                copy_mat[x][y] = 0
                    count_list.append(count)
                    count = 0

                final_list.append(sum(count_list))
                count_list.clear()
    print('{}'.format(max(final_list)))











######################################################################
# 요즘 A 형 문제는 먼저 문제의 앞부분에서 선택을 하고 뒷부분에서 풀이를 진행한 뒤, 
# 앞부분의 선택을 바꿔가면서 최대 최소값, 혹은 최적값을 찾는 문제가 많다. 
# 문제를 전체적으로 보면 완전탐색이 필요한 경우가 많음
# 보통 앞의 부분은 순열조합이 나오는 경우가 많다.
# 그리고 A형의 경우 앞의 문제보다 뒤의 문제가 쉬운 경우가 더 많다.


######################################################################
# 3 ≤ N, M ≤ 15
# 1 ≤ D ≤ 10
# N, M, D = 5, 15, 1

# # 우선 궁수의 위치선정에서 어떤 궁수가 어떤 자리에 온느지는 알 필요가 없다.
# # 궁수 세명을 놓을 위치만 잡으면 된다.
# for i in range(M -2):
#     for j in range(i + 1, M -1):
#         for k in range(j + 1, M):
#             print(i,j,k)


# # 거리가 D 이내이면서, 가장 가까운 적(t_i, t_j)를 찾는 법

# for i in range(N):
#     for j in range(M):
#         if tmp[i][j] == 1 and (abs(i - N) + abs(j - a)) <= D:
#             if (abs(i - N) + abs(j - a)) <= min_D:
#                 min_D = length