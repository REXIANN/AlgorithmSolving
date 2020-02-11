# 1258.py 행렬찾기
import pprint
import sys

sys.stdin = open("1258input.txt", "r")

# 그룹 1. n <= 10 이고 sub matrix의 개수 5개 이하
# 그룹 2. n <= 40 이고 5 < sub matrix <= 10
# 그룹 3. 40 < n <=80 이고 5 < sub matrix <= 10
# 그룹 4. 40 < n <=80 이고 10 < sub matrix <= 15
# 그룹 5. 80 < n<=100 이고 15 < sub matrix <= 20


tc = int(input())

for test_count in range(1, tc + 1):
    N_ = int(input())
    matrix = [[0] * (N_ + 2)]
    matrix.extend([[0] + list(map(int, input().split())) + [0] for _ in range(N_)])
    matrix.append([0] * (N_ + 2))
    sub_matrix = set()
    sum_list = []
    dr = [0, 1]
    dc = [1, 0]
    direction, i, j = 0, 1, 1

    for i in range(N_ + 1):

        for j in range(N_ + 1):

            if matrix[i][j] != 0:
                sub_row, sub_col = 0, 0
                row, col = i, j
                if matrix[row - 1][col] != 0 or matrix[row][col - 1] != 0:
                    continue

                while True:
                    sub_row += 1
                    row += dr[direction]
                    col += dc[direction]

                    if matrix[row][col] == 0:
                        row -= dr[direction]
                        col -= dc[direction]
                        direction = 1
                        break

                while True:
                    sub_col += 1
                    row += dr[direction]
                    col += dc[direction]

                    if matrix[row][col] == 0:
                        row -= dr[direction]
                        col -= dc[direction]
                        j = col
                        direction = 0
                        break

                sub_matrix.add((sub_col, sub_row))
    sub_matrix_list = sorted(list(sub_matrix))
    for sub_list in sub_matrix_list:
        sum_list.append(sub_list[0] * sub_list[1])
    
    
    print('#',test_count, len(sub_matrix), sub_matrix)
    print(sub_matrix_list)
    print(sum_list)