# 1216.py 회문2

import pprint
import sys
sys.stdin = open("1216input.txt", "r")
# 가장 긴 회문을 찾기

def longest_palin(matrix):
    length, result = 100, 0
    while True:
        for i in range(100):
            for j in range(0, 100 - length + 1):
                string = matrix[i][j:j + length]
                for n in range(length // 2):
                    if string[n] != string[-1-n]:
                        break
                else:
                     return length
        length -= 1


for test_count in range(1, 11):
    number = int(input())
    matrix = []
    for i in range(100):
        matrix.append(input())
    matrix_zip = list(map(''.join, zip(*matrix)))

    length = longest_palin(matrix)
    length2 = longest_palin(matrix_zip)
    print(max(length, length2), length, length2)
    