# 1215.py 회문
import pprint
import sys
sys.stdin = open("1215input.txt", "r")


tc = 10

for test_count in range(1, tc + 1):
    print('#', test_count, end=" ")
    length = int(input())
    matrix = []
    count = 0


    for i in range(8):
        matrix.append(input())
    #pprint.pprint(matrix)
    #print(matrix[3][3]
    zip_matrix = list(map(''.join, zip(*matrix)))
    #print(zip_matrix)

    for i in range(8):
        for j in range(9 - length):
            matrix_string = matrix[i][j:j + length]
            
            for k in range(length // 2):
                if matrix_string[k] != matrix_string[-1-k]:
                    break
            else:
                count += 1
                #print(matrix_string)
    #print(count)


    for i in range(8):
        for j in range(9 - length):
            matrix_string = zip_matrix[i][j:j + length]
            
            for k in range(length // 2):
                if matrix_string[k] != matrix_string[-1-k]:
                    break
            else:
                count += 1
                #print(matrix_string)
    print(count)