# 1697.py 숨바꼭질
import sys
sys.stdin = open("1697input.txt", "r")

def f(N, K, T = 0):
    global minV
    if T >= minV:
        return
    if N == K:
        minV = T if T < minV else minV
    else:
        f(N - 1, K, T + 1)
        f(N + 1, K, T + 1)
        f(N * 2, K, T + 1)

N, K = map(int, input().split())

minV = 50
f(N, K)
print(minV)