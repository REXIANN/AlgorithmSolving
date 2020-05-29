# 5251.py 최소 이동 거리
import sys
sys.stdin = open("5251input.txt", "r")
def backtrack(k, N, count=0):
    global minV
    if count > minV: return 
    if k == N:
        minV = count if count < minV else minV 
    else:
        for i in range(N + 1):
            if matrix[k][i]:
                backtrack(i, N, count + matrix[k][i])


for tc in range(int(input())):
    N, E = map(int, input().split())
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        r, c, v = map(int, input().split())
        matrix[r][c] = v
    minV = 10 * E
    backtrack(0, N)
    print('#{} {}'.format(tc + 1, minV))
