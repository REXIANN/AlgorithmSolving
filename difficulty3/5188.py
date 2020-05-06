# 5188.py  최소합
from pprint import pprint
import sys
sys.stdin = open("5188input.txt", "r")

dr = [0, 1] 
dc = [1, 0]
def backtrack(k, N, r, c, s):
    global minV
    if s > minV:
        return 
        
    if k == (N - 1) * 2:
        minV = s if s < minV else minV
    else:
        for i in range(2):
            rr, cc = r + dr[i], c + dc[i]
            if rr < N and cc < N:
                backtrack(k + 1, N, rr, cc, s + matrix[rr][cc])


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    minV = 10 * 13 * 2
    backtrack(0, N, 0, 0, matrix[0][0])
    print('#{} {}'.format(tc + 1, minV))
