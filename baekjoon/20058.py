import sys
sys.stdin = open('20058input.txt', 'r')

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N, Q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))
results = []

# STEP1. rotate and melt ice blocks
for line in L:
    # roatate matrix
    rotate_matrix = [[0] * 2 ** N for _ in range(2 ** N)]
    for i in range(0, 2 ** N, 2 ** line):
        for j in range(0, 2 ** N, 2 ** line):
            for k in range(2 ** line):
                for l in range(2 ** line):
                    rotate_matrix[i + l][j + 2 ** line  - 1 - k] = matrix[i + k][j + l]

    # deicing blocks
    matrix = [[0] * 2 ** N for _ in range(2 ** N)]
    for r in range(2 ** N):
        for c in range(2 ** N):
            count = 0
            for i in range(4):
                rr, cc = r + dr[i], c + dc[i]
                if 0 <= rr < 2 ** N and 0 <= cc < 2 ** N and rotate_matrix[rr][cc]:
                    count += 1           
            matrix[r][c] = rotate_matrix[r][c] - 1 if count < 3 else rotate_matrix[r][c]

            if matrix[r][c] < 0:
                    matrix[r][c] = 0

# STEP2. BFS runs to find the biggest ice block
dq = deque()
visited = [[False] * 2 ** N for _ in range(2 ** N)]
for r in range(2 ** N):
    for c in range(2 ** N):       
        count = 0      
        if not visited[r][c] and matrix[r][c]:
            visited[r][c] = True
            dq.append((r, c))
            count += 1
       
        while dq:
            r, c = dq.popleft()
            for i in range(4):
                rr, cc = r + dr[i], c + dc[i]
                if 0 <= rr < 2 ** N and 0 <= cc < 2 ** N and not visited[rr][cc] and matrix[rr][cc]:
                    visited[rr][cc] = True
                    dq.append((rr, cc))
                    count += 1
        
        if count:
            results.append(count)

print(sum([sum(matrix[i]) for i in range(2 ** N)])) # sum
print(max(results) if results else 0) # the biggest one