# 5215.py 햄버거 다이어트
import sys
sys.stdin = open("5215input.txt", "r")

def backtrack(k, N, L, cal=0, s=0):
    global maxV
    if cal > L: return
    maxV = s if s > maxV else maxV    
    for i in range(k, N):    
        backtrack(i + 1, N, L, cal + K[i], s + T[i])


for tc in range(int(input())):
    N, L = map(int, input().split())
    T, K = [0] * N , [0] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
    maxV = 0
    backtrack( 0, N, L)
    print('#{} {}'.format(tc + 1, maxV))