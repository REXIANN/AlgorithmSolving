# 4861.py 회문
import pprint
import sys
sys.stdin = open("4861input.txt", "r")

def target(N_, M_, matrix):
    target_str = ''
    for i in range(N_):
        for j in range(N_ - M_ + 1):
            temp = matrix[i][j:j + M_]
            if matrix[i][j:j + M_] == temp[::-1]:
                target_str = matrix[i][j:j + M_]
                return target_str
    return ''

tc = int(input())

for test_count in range(1, tc + 1):
    N_, M_ = map(int, input().split())
    matrix = []
    for _ in range(N_):
        matrix.append(input())

    matrix_zip = list(map(''.join, zip(*matrix)))
    
    target_str = target(N_, M_, matrix)
    if target_str == '':
        target_str = target(N_, M_, matrix_zip)
    print('#{} {}'.format(test_count, target_str))    

    
    
    
