# 5373.py 큐빙

import sys
sys.stdin = open("5373input.txt", "r")
couleurs = 'rbogwy' # Front, Right, Back, Left, Up, Down
F = [['r', 'r', 'r'],['r', 'r', 'r'],['r', 'r', 'r']]
D = [['y', 'y', 'y'],['y', 'y', 'y'],['y', 'y', 'y']]
B = [['o', 'o', 'o'],['o', 'o', 'o'],['o', 'o', 'o']]
U = [['w', 'w', 'w'],['w', 'w', 'w'],['w', 'w', 'w']]
L = [['g', 'g', 'g'],['g', 'g', 'g'],['g', 'g', 'g']]
R = [['b', 'b', 'b'],['b', 'b', 'b'],['b', 'b', 'b']]

dictionaire = {
    'F':'URDLU', 
    'D':'FRBLF', 
    'B':'DRULD', 
    'U':'BRFLB', 
    'L':'UFDBU', 
    'R':'ULDFU'
}

navigator = (
    ((0, 2), (1, 2), (2, 2)), # sud 
    ((0, 0), (1, 0), (2, 0)), # gauche
    ((0, 0), (0, 1), (0, 2)), # nord
    ((0, 2), (1, 2), (2, 2)), # droite
    ((0, 2), (1, 2), (2, 2))  # sud
)
position = ((0, 1, 2, 3, 4), (4, 3, 2, 1, 0))
move, temp = [], []
# start!
for _ in range(int(input())):
    count = int(input())
    ordre = input().split()
    for i in range(count):
        target, direction = dictionaire[ordre[i][0]], ordre[i][1]
        print(target, direction)
        direction = position[0] if direction == '+' else position[1]
        print(direction)
        # a, b, c = direction[0], direction[1], direction[2]
        print(ordre[i][0])
        # for idx in direction:
        #     s

            
