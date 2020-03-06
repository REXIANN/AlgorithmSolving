# for test
from pprint import pprint
import sys
sys.stdin = open("testinput.txt", "r")

def turn(matrix, t):
    mat = [[0] * 3 for _ in range(3)]
    if t == '-':
        for i in range(3):
            for j in range(3):
                mat[2-i][j] = matrix[j][i]
    elif t == '+':
        for i in range(3):
            for j in range(3):
                mat[i][j] = matrix[2-j][i]
    return mat


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mato = [[0] * 3 for _ in range(3)]
pprint(turn(matrix,'+'))

        
