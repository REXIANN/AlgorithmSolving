import pprint
import sys
sys.stdin = open("1210input.txt", "r")

for test_count in range(1, 11):
    number = int(input())
    matrix = []
    for _ in range(100):
        matrix.append(list(map(int,input().split())))
    
    front_line = [idx for idx, line in enumerate(matrix[0]) if line]
    end_point = matrix[99].index(2)
    