# 1861.py 정사각형 방
import sys
sys.stdin = open("1861input.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def f(r, c, N):
    used[r][c] = True

    global count
    for i in range(4):
        if -1 < r+dr[i] < N and -1 < c+dc[i] < N and not used[r+dr[i]][c+dc[i]] and matrix[r+dr[i]][c+dc[i]] -1 == matrix[r][c]:
            count += 1
            f(r+dr[i], c+dc[i], N)

for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    used = [[False] * N for _ in range(N)]
    lists = []
    r, c, count  = 0, 0, 0
    for i in range(N):
        for j in range(N):
            f(i, j, N)
            lists.append(count)
            count = 0
    print(lists)

