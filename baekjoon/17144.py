# 17144.py 미세먼지 안녕!
from pprint import pprint
import sys
sys.stdin = open("17144input.txt", "r")

import copy

R, C, T = map(int, input().split())
matrix = [[i for i in map(int, input().split())] for _ in range(R)]
ap_r, ap_r2 = tuple(i for i in range(R) if matrix[i][0])

sum_ = 0
dr = [-1, 0, 1, 0, 1, 0, -1, 0]
dc = [0, 1, 0, -1, 0, 1, 0, -1]

for h in range(T):
    matr = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if matrix[i][j] < 1: continue 
            matr[i][j] += matrix[i][j]

            for k in range(4):
                if 0 <= i+dr[k] < R and 0 <= j+dc[k] < C and matrix[i+dr[k]][j+dc[k]] != -1:
                    val = (matrix[i][j] // 5)
                    matr[i+dr[k]][j+dc[k]] += val
                    matr[i][j] -= val    

    r, c , k = ap_r - 1, 0, 0
    while k < 4:
        if 0 <= r+dr[k] < R and 0 <= c+dc[k] < C and r+dr[k] != ap_r2:
            pass
        else: 
            k += 1
            if k == 4: break
        matr[r][c] = matr[r+dr[k]][c+dc[k]]
        r, c = r+dr[k], c+dc[k]

    r, c = ap_r2 + 1, 0
    while k < 8:
        if 0 <= r+dr[k] < R and 0 <= c+dc[k] < C and r+dr[k] != ap_r:
            pass
        else:
            k += 1
            if k == 8: break
        matr[r][c] = matr[r+dr[k]][c+dc[k]]
        r, c = r+dr[k], c+dc[k]
    
    matr[ap_r][0], matr[ap_r2][0] = -1, -1
    matrix = copy.deepcopy(matr)
    
for i in range(R):
    sum_ += sum(matr[i])
print(sum_ + 2)


