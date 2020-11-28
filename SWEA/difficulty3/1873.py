# 1873.py 상호의 배틀필드
from pprint import pprint
import sys
sys.stdin = open("1873input.txt", "r")
tank     = '^>v<'
pos      = 'URDL'
road     = '.*#-'
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def f(R, C):
    for i in range(R):
        for j in range(C):
            if matrix[i][j] in tank:
                return i, j


def shoot(x, y, R, C):
    dir = tank.index(matrix[x][y])
    while 0 <= x + dr[dir] < R and 0 <= y + dc[dir] < C:
        x, y = x + dr[dir], y + dc[dir]
        if matrix[x][y] == '*':
            matrix[x][y] = '.'
            return
        elif matrix[x][y] == '#': 
            return


def move(x, y, command, R, C):
    matrix[x][y] = tank[pos.index(command)]
    dir = tank.index(matrix[x][y])
    if 0 <= x + dr[dir] < R and 0 <= y + dc[dir] < C:
        if matrix[x + dr[dir]][y + dc[dir]] == '.':
            x2, y2 = x + dr[dir], y + dc[dir]
            matrix[x][y], matrix[x2][y2] = matrix[x2][y2], matrix[x][y]
            return x2, y2
    return x, y


for tc in range(int(input())):
    R, C = map(int, input().split())
    matrix = [[i for i in input()] for _ in range(R)]
    N = int(input())
    commands = input()
    x, y = f(R, C)

    for command in commands:
        if command in pos:
            x, y = move(x, y, command, R, C)
        else:
            shoot(x, y, R, C)
    
    print('#{} '.format(tc+1), end='')
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end='')
        print()