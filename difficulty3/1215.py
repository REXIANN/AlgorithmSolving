# 1215.py 회문
import pprint
import sys
sys.stdin = open("1215input.txt", "r")


tc = 10

for test_count in range(1, tc + 1):
    length = int(input())
    matrix = []
    count = 0

    for i in range(8):
        matrix.append(input())
    #pprint.pprint(matrix)
    #print(matrix[3][3])

    for i in range(9 - length):
        for j in range(i, (i + length - 1) // 2):
            matrix_string = matrix[i][j:j + length]
            print(matrix_string)
            for k in range(j,(i + length - 1) // 2 )
                if matrix_string[j] != matrix_string[-1-j]:
                    break
                else:
                    count += 1

    for i in range(9 - length):
        for j in range(i, (i + length - 1) // 2):
            matrix_string = matrix[j:j + length][i]
            print(matrix_string)
            if matrix_string[j] != matrix_string[-1-j]:
                break
            else:
                count += 1

    print(count)