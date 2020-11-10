def solution(n, board):
    loc = [(0, 0)] * (n ** 2 + 1)
    answer = 0
    for i in range(n):
        for j in range(n):
            loc[board[i][j]] = (i, j)
    # print(loc)
    for i in range(len(loc) - 1):
        before = loc[i]
        after = loc[i + 1]
        # row
        row_normal = abs(before[0] - after[0])
        row_invert = abs(n - max(before[0], after[0])) + abs(min(before[0], after[0]))
        row_dis = row_normal if row_normal < row_invert else row_invert
        # col
        col_normal = abs(before[1] - after[1])
        col_invert = abs(n - max(before[1], after[1])) + abs(min(before[1], after[1]))
        col_dis = col_normal if col_normal < col_invert else col_invert

        distance = row_dis + col_dis + 1 # enter press
        answer += distance
        print(distance)
    return answer

n = 3
board = [[3, 5, 6], [9, 2, 7], [4, 1, 8]]
print(solution(n ,board))