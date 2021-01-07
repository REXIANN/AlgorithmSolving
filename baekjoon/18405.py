from collections import deque
import sys
sys.stdin = open('18405input.txt', 'r')

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
s, x, y = map(int, input().split())

print(N, K, s, x, y)
print(matrix)

# visited = [[False] * N for _ in range(N)]
dr = [-1 ,0, 1, 0]
dc = [0, 1, 0, -1]

print(visited)

for _ in range(s):
    for i in range(1, k + 1):
        for r in range(N):
            for c in range(N):
                
                if matrix[r][c] == i:
                    for i in range(4):
                        rr = r + dr[i]
                        cc = c + dc[i]
                        if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 0:
                            matrix[rr][cc] = i