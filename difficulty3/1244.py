# 1244.py 최대 상금
import sys
sys.stdin = open("1244input.txt", "r")

for tc in range(int(input())):
    N, T = input().split()
    N = [int(i) for i in N]
    print(tc+1, '\n', N)

    minI, maxI = len(N) - 1, len(N) - 2
    for i in range(len(N) - 1, 0, -1):
        if N[i] >= N[i - 1]: maxI = i; break
    for j in range(len(N) - 2):
        if N[j] <= N[j + 1]: minI = j; break
    
    N[minI], N[maxI] = N[maxI], N[minI]
    print(N)
    