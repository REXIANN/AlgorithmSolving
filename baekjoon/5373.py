# 5373.py 큐빙
from pprint import pprint
import sys
sys.stdin = open("5373input.txt", "r")
# couleurs = 'rbogwy' # Front, Right, Back, Left, Up, Down
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

cubes = {
    'F' : [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
    'D' : [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
    'B' : [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
    'U' : [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
    'L' : [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
    'R' : [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
}

dictionaire = {
    'F':'URDLU', 'D':'FRBLF', 'B':'DRULD', 
    'U':'BRFLB', 'L':'UFDBU', 'R':'ULDFU'
}

navigator = (
    ((0, 2), (1, 2), (2, 2)), # sud 
    ((0, 0), (1, 0), (2, 0)), # gauche
    ((0, 0), (0, 1), (0, 2)), # nord
    ((0, 2), (1, 2), (2, 2)), # droite
    ((0, 2), (1, 2), (2, 2))  # sud
)

position = ((1, 2, 3, 4), (3, 2, 1, 0))
move, temp = [], []

# start!
for _ in range(int(input())):
    count = int(input())
    ordre = input().split()
    for i in range(count):
        target, direction = dictionaire[ordre[i][0]], ordre[i][1]
        # print(target, direction)
        direction = position[0] if direction == '+' else position[1]
        # print(direction)
        for r, c in navigator[0]:
            move.append(cubes[target[0]][r][c])
        # print(move)
        
        print('panel', ordre[i][0], ordre[i][1], 'direction')
        for idx in direction: # +: 0 - 4 , -: 4 - 0
            for r, c in navigator[idx]:   
                temp = cubes[target[idx]][r][c]
                cubes[target[idx]][r][c] = move[navigator[idx].index((r, c))] 
                move[navigator[idx].index((r, c))] = temp
            for __ in range(3):
                print(cubes[target[idx]][__])
            print()
            # move.clear() 
        print('turn the matrix')
        for __ in range(3):
            print(cubes[ordre[i][0]][__])
        print()
        cubes[ordre[i][0]] = turn(cubes[ordre[i][0]], ordre[i][1])
        for __ in range(3):
            print(cubes[ordre[i][0]][__])
        print()

        print('this should be result')
        for __ in range(3):
            print(cubes['U'][__])
        print()