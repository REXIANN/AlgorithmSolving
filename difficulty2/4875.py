# 4875.py 미로
import sys
from pprint import pprint
sys.stdin = open("4875input.txt", "r")


tc = int(input())
for test_count in range(1, tc + 1):
    N = int(input())
    # N + 2 크기의 1로 둘러싸인 행렬을 만듬
    matrix = ['1' * (N + 2)]
    for _ in range(N):
        matrix.append(('1' + input() + '1'))
    matrix.append('1' * (N + 2))
    pprint(matrix)

    # 시작위치 찾음(1부터 시작하는 인덱스로 이루어진 좌표)
    for i in range(1, N + 1):
        if '2' in matrix[i]:
            row, col = i, matrix[i].index('2')
    #print(row, col)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    flag = 0
    stack = []
    visited = [[False for _ in range(N + 2)] for _ in range(N + 2)]
    pprint(visited)

    stack.append((row,col))
    while len(stack):
        row, col = stack.pop(-1)

        if visited[row][col] == False:
            visited[row][col] = True

        if flag:
            break

        for i in range(4):
            if matrix[row + dr[i]][col + dc[i]] == '0' and visited[row + dr[i]][col + dc[i]] == False:
                stack.append((row + dr[i], col + dc[i]))
            elif matrix[row + dr[i]][col + dc[i]] == '3':
                flag = 1

    print(flag)