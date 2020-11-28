# 알고리즘 모의고사 문제 1. 별자리
# import sys
# sys.stdin = open("SW_test_input.txt", "r")

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
def DFS(i, j):
    global count
    count += 1
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        M[x][y] = 0
        for i in range(8):
            xx, yy = x + dr[i], y + dc[i]
            if 0 <= xx < 10 and 0 <= yy < 10 and M[xx][yy]:
                stack.append((xx, yy))


for tc in range(int(input())):
    M = [list(map(int, input().split())) for _ in range(10)]
    count = 0
    X = [DFS(i, j) for i in range(10) for j in range(10) if M[i][j]]      
    print('#{} {}'.format(tc + 1, count))