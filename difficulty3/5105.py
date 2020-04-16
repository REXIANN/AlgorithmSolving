# 5105.py 미로의 거리
from pprint import pprint
import sys
sys.stdin = open("5105input.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def start(M, N):
    return [(i, j) for i in range(N) for j in range(N) if M[i][j] == '2']


def bfs(M, N, r, c):
    queue = []
    visited = [[0] * N for _ in range(N)]
    queue.append((r, c))
    visited[r][c] = 1

    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]
            if 0 <= rr < N and 0 <= cc < N:
                if visited[rr][cc] == 0:
                    if M[rr][cc] == '0':
                        queue.append((rr, cc))
                        visited[rr][cc] = visited[r][c] + 1
                    elif M[rr][cc] == '3':
                        return visited[r][c] - 1
    return 0


for tc in range(int(input())):
    N = int(input())
    M = [input() for _ in range(N)]
    starts = start(M, N)
    r, c = starts[0][0], starts[0][1]
    answer = bfs(M, N, r, c)
    print('#{} {}'.format(tc + 1, answer))