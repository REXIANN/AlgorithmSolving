# 5202.py 화물도크
import sys
sys.stdin = open("5202input.txt", "r")

def backtrack(a, k, N, cnt=0):
    global maxV
    maxV = cnt if cnt > maxV else maxV 
    for i in range(k, N):
        a_cp = a[:]
        if sum(a_cp[L[i][0]:L[i][1]]) == 0:
            a_cp[L[i][0]:L[i][1]] = [1] * (L[i][1] - L[i][0])
            backtrack(a_cp, i + 1, N, cnt + 1)


for tc in range(int(input())):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    backtrack([0 for _ in range(24)], 0, N)    
    print('#{} {}'.format(tc + 1, maxV))
