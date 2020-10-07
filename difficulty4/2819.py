# 2819.py 격자판의 숫자 이어붙이기
import sys
sys.stdin = open("2819input.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def f(r, c, k, s= ''):
    s += M[r][c]
    if k == 6: S.add(s)
    else:
        for i in range(4):
            if -1 < r+dr[i] < 4 and -1 < c+dc[i] < 4:
                f(r+dr[i], c+dc[i], k+1, s)

for tc in range(int(input())):
    M = [input().split() for _ in range(4)]
    S = set()
    for i in range(4):
        for j in range(4):
            f(i, j, 0)
    print('#{} {}'.format(tc+1, len(S)))