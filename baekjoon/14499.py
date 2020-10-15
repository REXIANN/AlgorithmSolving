import sys
sys.stdin = open("14499input.txt", "r")

N, M, r, cc, K = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
route = list(map(int, input().split()))
for i in route:
    if 0 <= r + dr[i - 1] < N and 0 <= cc + dc[i - 1] < M:
        r = r + dr[i - 1]
        cc = cc + dc[i - 1]
        if i == 1:
            a, b, c, d, e, f = d, b, a, f, e, c
        elif i == 2:
            a, b, c, d, e, f = c, b, f, a, e, d
        elif i == 3:
            a, b, c, d, e, f = e, a, c, d, f, b
        elif i == 4:
            a, b, c, d, e, f = b, f, c, d, a, e
        
        if g[r][cc] == 0:
            g[r][cc] = f
        else:
            f = g[r][cc]
            g[r][cc] = 0
        
        print(a)
