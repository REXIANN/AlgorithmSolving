# 1226.py 미로
import pprint
import sys
sys.stdin = open("1226input.txt", "r")


def find_next(row, column):
    dr = [-1, 0, 1, 0]
    dc = [ 0, 1, 0, -1]

    for i in range(4):
        if maze[row + dr[i]][column + dc[i]] == '0' and not visited[row + dr[i]][column + dc[i]]:
            return row + dr[i], column + dc[i]
        elif maze[row + dr[i]][column + dc[i]] == '3':
            return -1, -1
    return row, column


def DFS(row, column):
    flag = 0
    visited[row][column] = True
    stack.append((row, column))
    while len(stack) > 0:
        wr, wc = find_next(row, column)


        while not(wr == row and wc == column):
            stack.append((wr, wc))
            visited[wr][wc] = True
            #stack.append([wr, wc])
            row, column = wr, wc
            wr, wc = find_next(row, column)
            if wr == -1 and wc == -1:
                flag = 1
                break

        if flag: break
        row, column = stack.pop(-1)
    return flag


for test_count in range(1, 11):
    nth = int(input())
    maze = [input() for _ in range(16)]
    pprint.pprint(maze)

    # 지나가는 경로를 체크하는 visited 배열 생성
    visited = [[i != '0' for i in line] for line in maze]
    stack = []

    # 시작점 row, col 찾음
    for i, line in enumerate(maze):
        if '2' in line:
            row, col = i, line.index('2')

    flag = DFS(row, col)
    print('#{} {}'.format(test_count, flag))


