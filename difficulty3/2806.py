# 2806.py N-Queen
import sys
sys.stdin = open("2806input.txt", "r")

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def queen(r, c, N):
    global count
    if r == N:
        count += 1
    else:
        if visited[r][c]: return

        visited[r][c] = True

        for i in range(8):
            rr, cc = r, c
            while True:
                if 0 <= rr + dr[i] < N and 0 <= cc + dc[i] < N:
                    visited[rr + dr[i]][cc + dc[i]] = True
                    rr, cc = rr + dr[i], cc + dc[i]
                else:
                    break
        
        for i in range(N):
            queen(r + 1, i, N)

for tc in range(int(input())):
    N = int(input())
    M = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        queen(0, i, N)
    print(count)