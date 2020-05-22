from pprint import pprint
import sys

sys.stdin = open("13460input.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bt(k, idx, r_r, r_c, b_r, b_c):
    global minV
    # 최솟값 비교
    if k > minV: 
        return 
    for i in range(4):
        if idx == i: 
            continue

        result = 999
        r_flag, b_flag, r_conf, b_conf = 1, 1, 1, 1
        r_rr, r_cc, b_rr, b_cc = r_r, r_c, b_r, b_c
        while r_flag | b_flag:
            # 빨간공 이동 - 골인하면 confirm 0 만듬 - 허가
            if 0 <= r_rr + dr[i] < N and 0 <= r_cc + dc[i]< M:
                if mat[r_rr + dr[i]][r_cc + dc[i]] == '.':
                    r_rr, r_cc = r_rr + dr[i], r_cc + dc[i]
                elif mat[r_rr + dr[i]][r_cc + dc[i]] == 'O':
                    r_rr, r_cc = r_rr + dr[i], r_cc + dc[i]
                    r_conf = 0
                else:
                    r_flag = 0
            # 파란공 이동 - 골인하면 confirm 1 만듬 - 방지
            if 0 <= b_rr + dr[i] < N and 0 <= b_cc + dc[i]< M:
                if mat[b_rr + dr[i]][b_cc + dc[i]]  == '.':
                    b_rr, b_cc = b_rr + dr[i], b_cc + dc[i]
                elif mat[b_rr + dr[i]][b_cc + dc[i]]  == 'O':
                    b_rr, b_cc = b_rr + dr[i], b_cc + dc[i]
                    b_conf = 0
                else:
                    b_flag = 0

        if b_conf == 0:
            continue
        # if r_conf == 0 and b_conf == 0:
        #     continue
        # if r_conf == 1 and b_conf == 0:
        #     return
        if r_conf == 0 and b_conf == 1:
            result = k
        # 만일 두공의 위치가 같으면 r-r, r-c, b-r, b-c 비교하여 위치 재정렬
        if r_rr == b_rr and r_cc == b_cc:
            if r_r < r_rr or b_r < b_rr: # 공이 아래로 내려간 경우, dr[i] = 1
                if r_r > b_r: 
                    b_rr -= dr[i]
                elif b_r > r_r:
                    r_rr -= dr[i]
            elif r_r > r_rr or b_r > b_rr: # 공이 위로 올라간 경우, dr[i] = -1
                if r_r > b_r:
                    r_rr -= dr[i]
                elif b_r > r_r:
                    b_rr -= dr[i]
            elif r_c < r_cc or b_c < b_cc: # 공이 오른쪽으로 간 경우 dc[i] = 1
                if r_c > b_c:
                    b_cc -= dc[i]
                elif b_c > r_c:
                    r_cc -= dc[i]
            elif r_c > r_cc or b_c > b_cc: # 공이 왼쪽으로 간 경우 dc[i] = -1
                if r_c > b_c:
                    r_cc -= dc[i]
                elif b_c > r_c:
                    b_cc -= dc[i]
        # 두 공의 위치변화가 없으면 이미 최적화에 실패했으므로 더 이상 진행할 필요없다
        if r_rr == r_r and r_cc == r_c and b_rr == b_r and b_cc == b_c: 
            continue
        # 이동이 완료되면 다음 무브로 진행
        minV = result if result < minV else minV
        bt(k + 1, i, r_rr, r_cc, b_rr, b_cc)


N, M = map(int, input().split())
mat = [[char for char in input()] for _ in range(N)]
# pprint(mat)
red_position = [(r, c) for r in range(N) for c in range(M) if mat[r][c] == 'R']
blue_position = [(r, c) for r in range(N) for c in range(M) if mat[r][c] == 'B']
# R과 B의 위치를 찾고 인덱스를 저장한 뒤 지도에서 없앰
r_r, r_c = red_position[0][0], red_position[0][1]
b_r, b_c = blue_position[0][0], blue_position[0][1]
mat[r_r][r_c], mat[b_r][b_c] = '.', '.'
# pprint(mat)
minV = 11
bt(1, 4, r_r, r_c, b_r, b_c)
print(-1 if minV >= 11 else minV)
