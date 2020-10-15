from pprint import pprint
# 14503.py 로봇 청소기
N, M = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

flag = True
count = 0
while flag:
    # 1. clean current position
    # print(r, c, d)
    if not matrix[r][c]:
        matrix[r][c] = 2
        count += 1

    for i in range(1, 5):
        dd = d - i
        if dd < 0:
            dd = 4 + dd

        rr, cc = r + dr[dd], c + dc[dd]
        # if not a wall
        if matrix[rr][cc] != 1:
            # print('rcd', rr, cc, dd)
            # if not cleaned
            if matrix[rr][cc] != 2:
                r, c = rr, cc
                d = dd
                break
            # if cleaned
            else:
                continue
        # if a wall
        else:
            continue
    else:
        for i in range(1, 3):
            dd = d - i
            if dd < 0:
                dd = 4 + dd
        # go back
        rr, cc = r + dr[dd], c + dc[dd]
        # if backyard is okay
        if matrix[rr][cc] != 1:
            r, c = rr, cc
        elif matrix[rr][cc] == 1:
            flag = False

    # for i in range(N):
    #     print(matrix[i])
    # print()

print(count)
