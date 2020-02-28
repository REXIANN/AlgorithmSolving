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
