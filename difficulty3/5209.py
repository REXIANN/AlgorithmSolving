# 5209.py 최소생산비용
import sys
sys.stdin = open("5209input.txt", "r")

def backtrack(a, k, N, total=0):
    global minV
    if total > minV: return
    if k == N:
        minV = minV if minV < total else total
    else:
        in_perm = [False] * N
        for i in range(0, k):
            in_perm[a[i]] = True

        for i in range(N):
            if not in_perm[i]:
                a[k] = i
                backtrack(a, k+1, N, total+matrix[k][i])
                

for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    minV = 99 * N
    backtrack([0] * N, 0, N)
    print('#{} {}'.format(tc + 1, minV))
