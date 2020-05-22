# 1926.py 그림
import sys
sys.stdin = open("1926input.txt", "r")

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def bfs(i, j, N, M):
    dq = deque()
    dq.append((i, j))
    matrix[i][j] = 0
    value = 1 
    while dq:
        ii, jj = dq.popleft()
        for i in range(4):
            i_d, j_d = ii + dr[i], jj + dc[i]
            if 0 <= i_d < N and 0 <= j_d < M:
                if matrix[i_d][j_d]:
                    dq.append((i_d, j_d))
                    value += 1
                    matrix[i_d][j_d] = 0
    return value


N, M = tuple(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]
result = [bfs(i, j, N, M) for i in range(N) for j in range(M) if matrix[i][j]]
print(len(result))
print(max(result) if result else 0)
