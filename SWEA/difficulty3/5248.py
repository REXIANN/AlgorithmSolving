# 5248.py 그룹 나누기
from pprint import pprint
import sys
sys.stdin = open("5248input.txt", "r")

def dfs(i, N):
    visited[i] = True
    for j in range(N + 1):
        if matrix[i][j]:
            matrix[i][j] = 0
            dfs(j, N)


for tc in range(int(input())):
    N, M = map(int,input().split())
    L = list(map(int, input().split()))
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(0, M * 2, 2):
        matrix[L[i]][L[i + 1]] = 1
        matrix[L[i + 1]][L[i]] = 1 
    # pprint(matrix)
    count = 0
    visited = [False] * (N + 1)
    for i in range(N + 1):
        if not visited[i]:
            count += 1
            visited[i] = True
            dfs(i, N)

    print('#{} {}'.format(tc + 1, count - 1))
