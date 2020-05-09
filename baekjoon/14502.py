# 14502.py 연구소
from pprint import pprint
import sys
sys.stdin = open("14502input.txt", "r")
# 정답은 1번: 27, 2번: 9, 3번: 3
import queue
import copy
from itertools import combinations

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# print(N, M)
# pprint(matrix)
q = queue.Queue()
walls = [(r, c) for r in range(N) for c in range(M) if matrix[r][c] == 0]
minV = N * M
result = 0
for w1, w2, w3 in combinations(walls, 3):
    matr = copy.deepcopy(matrix)
    count1, count2 = 0, 0
    matr[w1[0]][w1[1]] = 1
    matr[w2[0]][w2[1]] = 1
    matr[w3[0]][w3[1]] = 1

    for r in range(N):
        for c in range(M):
            if matr[r][c] == 2:
                q.put((r, c))
                count2 += 1
            elif matr[r][c] == 1:
                count1 += 1
    
    while not q.empty():
        q_rc = q.get()
        q_r, q_c = q_rc[0], q_rc[1]
        for i in range(4):
            q_rr, q_cc = q_r + dr[i], q_c + dc[i]
            if 0 <= q_rr < N and 0 <= q_cc < M:
                if not matr[q_rr][q_cc]:
                    matr[q_rr][q_cc] = 2
                    count2 += 1
                    q.put((q_rr, q_cc))
    safe_area = N * M - count1 - count2
    result = safe_area if safe_area > result else result
print(result)
