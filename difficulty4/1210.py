import pprint
import sys
sys.stdin = open("1210input.txt", "r")

for test_count in range(1, 11):
    number = int(input())
    matrix = [[0 for _ in range(102)]]
    for _ in range(100):
        matrix.append([0] + list(map(int,input().split())) + [0])

    ends = [idx for idx, line in enumerate(matrix[1]) if line]
    start = matrix[100].index(2)
    row = 101
    idx = ends.index(start)
    while True:
        row -= 1
        if matrix[row][start - 1] == 1:
            idx -= 1
            start = ends[idx]
            continue

        if matrix[row][start + 1] == 1:
            idx += 1
            start = ends[idx]
            continue

        if matrix[row - 1][start] == 0:
            print('#{} {}'.format(number, ends[idx] - 1))
            break

        

    
    
    
    
    
    