# 19236.py 청소년상어
import sys
sys.stdin = open('19236input.txt', 'r')

import copy
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

# 물고기들 순회
def fish_move(i, matrix_fish):
    rc = [(r, c) for c in range(4) for r in range(4) if matrix_fish[r][c] == i]
    if len(rc) == 0:
        return matrix_fish
    r, c = rc[0][0], rc[0][1]
    fish = matrix_fish[r][c]
    idx = 0
    while idx < 8:
        f_d = fish_dir[fish]
        f_d = (f_d + idx) % 8
        idx += 1
        rr, cc = r + dr[f_d], c + dc[f_d]
        if 0 <= rr < 4 and 0 <= cc < 4 and matrix_fish[rr][cc] < 17:
            matrix_fish[r][c], matrix_fish[rr][cc] = matrix_fish[rr][cc], matrix_fish[r][c]
            fish_dir[fish] = f_d
            return matrix_fish
    return matrix_fish

# 상어가 먹이를 찾아 이동
def shark_move(r, c, matrix_shark, fish_dir, shark_dir, fish_count):
    global maxV

    for i in range(4):
        for j in range(4):
            if matrix_shark[i][j] == 17:
                matrix_shark[i][j] = 0
    fish = matrix_shark[r][c]
    shark_dir = fish_dir[fish]
    fish_count += fish
    matrix_shark[r][c] = 17
    maxV = fish_count if fish_count > maxV else maxV

    for i in range(1, 17):
        matrix_shark = fish_move(i, matrix_shark)
    
    for i in range(4):
        print(matrix_shark[i])
    print(fish_count)
    print()

    for i in range(1, 4):
        rr, cc = r + dr[shark_dir] * i, c + dc[shark_dir] * i
        if 0 <= rr < 4 and 0 <= cc < 4 and matrix_shark[rr][cc] > 0:
            temp = copy.deepcopy(matrix_shark)
            temp2 = fish_dir[:]
            shark_move(rr, cc, matrix_shark, fish_dir, shark_dir, fish_count)
            matrix_shark = temp
            fish_dir = temp2
            

# 메인문
fish_dir = [0] * 17
matrix = [[0] * 4 for _ in range(4)]
idx = 0
for _ in range(4):
    fishes = list(map(int, input().split()))
    for i in range(0, len(fishes), 2):
        r, c = idx // 4, idx % 4
        matrix[r][c] = fishes[i]
        fish_dir[fishes[i]] = fishes[i + 1] - 1
        idx += 1
maxV = 0
shark_move(0, 0, matrix, fish_dir, 0, 0)
print(maxV)
