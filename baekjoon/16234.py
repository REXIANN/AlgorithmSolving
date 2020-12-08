# 16234.py 인구 이동
import sys
sys.stdin = open("16234input.txt", "r")

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(i, j, L, R, N):
    q = deque()
    q.append((i, j))
    flag = 0
    arr = [(i, j)]
    count = matrix[i][j]
    visited[i][j] = True
    while q:
        x = q.popleft()
        ii, jj = x[0], x[1]
        for i in range(4):
            i_d, j_d = ii + dr[i], jj + dc[i]
            if 0 <= i_d < N and 0 <= j_d < N:
                diff = abs(matrix[ii][jj] - matrix[i_d][j_d])
                if not visited[i_d][j_d] and L <= diff <= R:
                    flag += 1
                    q.append((i_d, j_d))
                    visited[i_d][j_d] = True
                    count += matrix[i_d][j_d]
                    arr.append((i_d, j_d))
    value = count // len(arr)
    for pp in arr:
        matrix[pp[0]][pp[1]] = value
    return 1 if flag > 0 else 0


N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = 0
count = 0
while True:
    re = result
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result += bfs(i, j, L, R, N)
    res = result
    if (res - re) == 0:
        break
    else:
        count += 1

print(count)

