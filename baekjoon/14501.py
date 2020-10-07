# 14501.py 퇴사
import sys
sys.stdin = open("14501input.txt", "r")
def backtrack(k, N, s=0):
    if k > N: return
    global maxV
    maxV = s if s > maxV else maxV
    for i in range(k, N):
        backtrack(i + T[k], N, s + P[k])
    

N = int(input())
T, P = [0] * N, [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())
maxV = -1
for i in range(N): backtrack(i, N)
print(maxV)