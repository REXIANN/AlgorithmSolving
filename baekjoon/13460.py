from pprint import pprint
import sys
sys.settrace
# sys.setrecursionlimit(4 ** 10)
sys.stdin = open("13460input.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bt(k, idx, r_r, r_c, b_r, b_c):
    global minV
    if k > minV: return 
        # 최솟값 비교
    for i in range(4):
        if idx == i: continue

        result = 999
        r_flag, b_flag, confirm = 1, 1, 1
        r_rr, r_cc, b_rr, b_cc = r_r, r_c, b_r, b_c
        while r_flag | b_flag | confirm:
            r_rr
        # 이동이 완료되면 다음 무브로 진행
        minV = result if result < minV else minV
        bt(k + 1, N, i, r_rr, r_cc, b_rr, b_cc)


N, M = map(int, input().split())
mat = [[char for char in input()] for _ in range(N)]
# pprint(mat)
red_position = [(r, c) for r in range(N) for c in range(M) if mat[r][c] == 'R']
blue_position = [(r, c) for r in range(N) for c in range(M) if mat[r][c] == 'B']
# R과 B의 위치를 찾고 인덱스를 저장한 뒤 지도에서 없앰
r_r, r_c = red_position[0][0], red_position[0][1]
b_r, b_c = blue_position[0][0], blue_position[0][1]
mat[r_r][r_c], mat[b_r][b_c] = '.', '.'
pprint(mat)
minV = 10
bt(0, 4, r_r, r_c, b_r, b_c)
print(-1 if minV == 11 else minV)
