# 3752.py 가능한 시험점수
import sys
sys.stdin = open("3752input.txt", "r")

for tc in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    T = []
    S = set()
    for i in range(1 << N):
        X = 0
        for j in range(N):
            if i & (1 << j):
                X += L[j]
        if X in S:
            break
        S.add(X)
    
    print('set result:', len(S), '\n', S)
    # print('#{} {}'.format(tc+1, len(S)))




    
    # def f(k, n, s):
    # if s in S:
    #     return
    # else:
    #     S.add(s)
    
    # if k == n:
    #    pass
    # else: 
    #     for i in range(k, n):
    #         f(k+i, n, s+L[i])