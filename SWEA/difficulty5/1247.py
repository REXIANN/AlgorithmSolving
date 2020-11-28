# 1247.py 최적 경로
import sys
sys.stdin = open("1247input.txt", "r")

from itertools import permutations
def bt(k, N, cnt):
    global minV
    if cnt > minV: return
    if k==N:
        minV = cnt if cnt < minV else minV
    else:
        val = abs(R[k][0] - R[k - 1][0]) + abs(R[k][1] - R[k -1][1])
        bt(k + 1, N, cnt + val)


for tc in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    r1, c1, r2, c2 = L[0], L[1], L[2], L[3]
    clients = [(L[2 * i], L[2 * i + 1]) for i in range(2, N + 2)]
    minV = 100 * N
    for R in permutations(clients):
        value = abs(r1 - R[0][0]) + abs(c1 - R[0][1]) + abs(r2 - R[-1][0]) + abs(c2 - R[-1][1])
        bt(1, N, value)
    print('#{} {}'.format(tc + 1, minV))
