# 31. 금광
import sys
sys.stdin = open('31input.txt', 'r')

for _ in range(int(input())):
    N, M = map(int, input().split())
    mine = list(map(int, input().split()))
    matrix = [mine[M * i:M * i + M] for i in range(N)]
    result = [[0 for i in range(M)] for j in range(N)]

    for i in range(N):
        result[i][0] = matrix[i][0] 

    for r in range(1, N):
        for c in range(M):


    print(result)
    print(matrix)
