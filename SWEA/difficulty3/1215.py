# 1215.py 회문
import pprint
import sys
sys.stdin = open("1215input.txt", "r")


def is_palin1(list_, length):
    count = 0
    for i in range(len(list_) - length + 1):
        string = list_[i : i + length]
        if string == string[::-1]:
            count += 1
    return count


def calc(matrix, length):
    count = 0
    for lists in matrix:
        count += is_palin1(lists, length)
    return count


for test_count in range(1, 11):
    length = int(input())
    matrix = []
    for i in range(8):
        matrix.append(input())
    #pprint.pprint(matrix)
    matrix_zip = list(map(''.join, zip(*matrix)))
    count = calc(matrix, length) + calc(matrix_zip, length)
    print('#{} {}'.format(test_count, count))