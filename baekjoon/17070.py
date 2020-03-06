# 17070.py 파이프옮기기 1
import sys
sys.stdin = open("17070input.txt", "r")
# mod = 1:가로 2:세로 3:대각선
# mov = 1:가로였음 2:세로였음 3:대각선이었음
def dfs(r, c, N, mod=1):
    global count
    if r == N or c == N: return
    if matrix[r][c]: return

    if r == N-1 and c ==  N-1:
        count += 1
    else:
        if mod == 1:
            if c+1 < N:
                dfs(r, c+1, N, 1)
                if r+1 < N and matrix[r][c+1] == 0:
                    dfs(r+1, c+1, N, 3)
        elif mod == 2:
            if r+1 < N :
                dfs(r+1, c, N, 2)          
                if c+1 < N and matrix[r+1][c] == 0:
                    dfs(r+1, c+1, N, 3)
        elif mod == 3:
            dfs(r+1, c+1, N, 3)
            if r+1 < N:
                dfs(r+1, c, N, 2)
                if c+1 < N:
                    dfs(r, c+1, N, 1)
        
            

for _ in range(4):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    dfs(0, 1, N)
    print(count)
    