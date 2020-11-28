# 1251.py 하나로
import sys
sys.stdin = open("1251input.txt", "r")

def backtrack(k, E, N, s=0):
    global minV
    if s > minV: return
    if k == N:

        minV = round(s) if s < minV else minV
    else: 
        for i in range(k):
            visited[A[i]] = True
        
        for i in range(N):
            if not visited[i]:
                A[k] = i
                cost = E * (abs(X[k] - X[i]) ** 2 + abs(Y[k] - Y[i]) ** 2)
                print(cost)
                backtrack(k + 1, E, N, s + cost)
                visited[i] = False


for tc in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    A = [0] * N
    visited = [0] * N
    minV = 10 ** 15
    backtrack(0, E, N)
    print('#{} {}'.format(tc + 1, minV))
