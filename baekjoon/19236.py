# 19236.py 청소년상어
import copy
import sys
sys.stdin = open('19236input.txt', 'r')

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fishes(matrix):
    result = [0] * 16
    for i in range(4):
        for j in range(4):
            f, d = matrix[i][j][0], matrix[i][j][1] 
            result[f] = d
    return result


matrix = []
for i in range(4):
    orders = list(map(int, input().split()))
    # 실제 숫자가 1 ~ 16 이므로 1씩 빼줘야 함
    arr = [(orders[j] - 1, orders[j + 1]) for j in range(0, 8, 2)]
    matrix.append(arr)
print(matrix)

fish_dir = find_fishes(matrix)
print(fish_dir)