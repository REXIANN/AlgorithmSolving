# 1954.py 달팽이 숫자

import pprint
import sys
sys.stdin = open("1954input.txt", "r")

# 달팽이의 크기 N은 1이상 10이하의 정수이다. (N= 1~ 10)

# 1 2 3
# 8 9 4
# 7 6 5

#  1  2  3  4
# 12 13 14  5
# 11 16 15  6
# 10  9  8  7



###########################################
import pprint

def isWall(x, y):
    if x < 0 or x >= 10: return True
    if y < 0 or y >= 10: return True
    if array[x][y] != 0: return True
    return False


X, Y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
array = [[0 for _ in range(10)] for _ in range(10)]
dir_stat = 0  # 0:오른쪽, 1:아래, 2:왼쪽, 3:위

for i in range(1, 101):
    array[X][Y] = i
    X += dx[dir_stat]
    Y += dy[dir_stat]


    if isWall(X, Y):
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = (dir_stat + 1) % 4
        X = X + dx[dir_stat]
        Y = Y + dy[dir_stat]

pprint.pprint(array)

