# 3055.py 탈출
from pprint import pprint
import sys
sys.stdin = open("3055input.txt", "r")

import copy
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def maze(M, k, R, C, r, c, water):
    MM = copy.deepcopy(M)
    water2 = []
    while water:
        rr, cc = water.pop()
        for i in range(4):
            if MM[rr + dr[i]][cc + dc[i]] == '.':
                MM[rr + dr[i]][cc + dc[i]] = '*'
                water2.append((rr + dr[i], cc + dc[i]))

    for i in range(4):
        ri, ci = r + dr[i], c + dc[i]
        if MM[ri][ci] == '.':
            MM[ri][ci] = 'S'
            maze(MM, k + 1, R, C, ri, ci, water2)
        elif MM[ri][ci] == 'D':
            global result
            result = k + 1
            return

     
R, C = map(int, input().split())
M = [['X'] * (C + 2)]
for _ in range(R):
    arr = ['X']
    for i in input():
        arr.append(i)
    arr.append('X')
    M.append(arr)
M.append(['X'] * (C + 2))

result = 'KAKTUS'
S = [(r, c) for r in range(1, R + 1) for c in range(1, C + 1) if M[r][c] == 'S']
water = [(i,j) for i in range(1, R + 1) for j in range(1, C + 1) if M[i][j] == '*']
maze(M, 0, R, C, S[0][0], S[0][1], water)
print(result)