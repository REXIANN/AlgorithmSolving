import sys
sys.stdin = open('20058input.txt', 'r')

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N, Q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))
results = []

# print(N, Q, L)
# print(matrix)
# print(sum([sum(matrix[i]) for i in range(2 ** N)]))

# STEP1. rotate and melt ice blocks
for line in L:
    # L길이만큼 얼음들 회전 실행 -> for
    rotate_matrix = [[0] * 2 ** N for _ in range(2 ** N)]
    for i in range(0, 2 ** N, 2 ** line):
        for j in range(0, 2 ** N, 2 ** line):
            for k in range(2 ** line):
                for l in range(2 ** line):
                    rotate_matrix[i + l][j + 2 ** line  - 1 - k] = matrix[i + k][j + l]
    
    # for i in range(2 ** N):
    #     print(matrix[i])
    # print()
    
    # for i in range(2 ** N):
    #     print(rotate_matrix[i])
    # print()
    matrix = [[0] * 2 ** N for _ in range(2 ** N)]

    # 인접한 부분 얼음 체크해서 녹이기
    for r in range(2 ** N):
        for c in range(2 ** N):
            count = 0
            for i in range(4):
                rr, cc = r + dr[i], c + dc[i]
                if 0 <= rr < 2 ** N and 0 <= cc < 2 ** N and rotate_matrix[rr][cc]:
                    count += 1
            
            if count < 3:
                matrix[r][c] = rotate_matrix[r][c] - 1
                if matrix[r][c] < 0:
                     matrix[r][c] = 0
            else:
                matrix[r][c] = rotate_matrix[r][c]

    # for i in range(2 ** N):
    #     print(matrix[i])
    # print()

# print(sum([sum(matrix[i]) for i in range(2 ** N)]))

# 얼음의 총합
# BFS로 돌려서 얼음의 총합 세야됨 BFS로 돌린 결과 리스트에 넣고 max한개, sum한개
dq = deque()
visited = [[False] * 2 ** N for _ in range(2 ** N)]
for r in range(2 ** N):
    for c in range(2 ** N):
        count = 0
        if not visited[r][c] and matrix[r][c]:
            visited[r][c] = True
            dq.append((r, c))
            count += 1
        # print('init', dq)
        while dq:
            r, c = dq.popleft()
            for i in range(4):
                rr, cc = r + dr[i], c + dc[i]
                if 0 <= rr < 2 ** N and 0 <= cc < 2 ** N and not visited[rr][cc] and matrix[rr][cc]:
                    # print('rol', dq, count)
                    dq.append((rr, cc))
                    visited[rr][cc] = True
                    count += 1
        
        if count:
            results.append(count)

# print(results)
print(sum([sum(matrix[i]) for i in range(2 ** N)]))
print(max(results) if results else 0)
# 남아있는 얼음의 합 sum(A[r][c])
# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 count(max(A[r][c]))