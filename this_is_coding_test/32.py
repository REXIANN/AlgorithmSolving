# 32. 정수 삼각형
import sys
sys.stdin = open('32input.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for i in range(N)]

for i in range(1, N):
    for j in range(len(L[i])):
        x, y = j - 1, j
        if 0 <= x < len(L[i]):
            x = L[i - 1][j - 1]
        else:
            x = 0
        
        if 0 <= y < len(L[i - 1]):
            y = L[i - 1][j]
        else:
            y = 0

        L[i][j] = L[i][j] + max(x, y)

print(max(L[-1]))
