import sys
sys.stdin = open('18405input.txt', 'r')
from collections import deque

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
s, x, y = map(int, input().split())

dr = [-1 ,0, 1, 0]
dc = [0, 1, 0, -1]
dq = deque()

count = 0
for i in range(1, K + 1):
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == i:
                dq.append((r, c, i))
                count += 1

for _ in range(s):
    inner_count = 0
    for _ in range(count):
        r, c, i = dq.popleft()
        for j in range(4):
            rr = r + dr[j]
            cc = c + dc[j]
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 0:
                matrix[rr][cc] = i
                dq.append((rr, cc, i))
                inner_count += 1
    count = inner_count

print(matrix[x - 1][y - 1])