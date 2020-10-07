# 1865.py 동철이의 일 분배
from pprint import pprint
import sys
sys.stdin = open("1865input.txt", "r")

def f(k, N, s):
    global maxV
    if s <= maxV:
        return
    
    if k == N:
        maxV = s if maxV < s else maxV
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                f(k+1, N, s * (matrix[k][i] / 100))
                used[i] = 0
                

for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    maxV = 0
    f(0, N, 1)
    print('#{} {:6f}'.format(tc+1, maxV * 100))


# DP를 이용한 풀이
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     M = 1 << N
#     dp = [[0.0 for _ in range(M)] for _ in range(N)]
 
#     G = []
#     for i in range(N):
#         G.append(list(map(float, input().split())))
#         for j in range(N):
#             G[i][j] = G[i][j] / 100
 
#     for i in range(N):
#         dp[0][1 << i] = G[0][i]
 
#     for i in range(1, N):
#         for cur in range(1, M):
#             if dp[i - 1][cur] == 0:
#                 continue
 
#             for j in range(N):
#                 if cur & (1 << j) != 0 or G[i][j] == 0:
#                     continue
#                 next = cur | (1 << j)
 
#                 dp[i][next] = max(dp[i][next], dp[i - 1][cur] * G[i][j])
 
#     print("#%d %.6f" % (test_case, dp[N - 1][M - 1]*100))