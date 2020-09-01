# 5521.py 상원이의 생일파티
from pprint import pprint
import sys
sys.stdin = open("5521input.txt", "r")

def bfs(x, N):
    for i in range(1, N):
        if matrix[x][i] and not matrix[0][i]:
            matrix[0][i] = 2

            
for tc in range(int(input())):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]
    for _ in range(M):
        r, c = map(int, input().split())
        matrix[r - 1][c - 1] = 1
        matrix[c - 1][r - 1] = 1
    result = [bfs(i, N) for i in range(1, N) if matrix[0][i] == 1]
    cnt = matrix[0][1:].count(0)
    print('#{} {}'.format(tc + 1,N - 1 - cnt))
