# 3349.py 최솟값으로 이동하기

import sys
sys.stdin = open("3349input.txt", "r")
    
for tc in range(int(input())):
    W, H, N = map(int, input().split())
    x1, y1 = map(int, input().split())
    cost = 0
    for _ in range(N - 1):
        x2, y2 = map(int, input().split())
        X, Y = abs(x2-x1), abs(y2-y1)
        cost += max(X, Y) if (x2>x1 and y2>y1) or (x2<x1 and y2<y1) else X + Y
        x1, y1 = x2, y2
    print('#{} {}'.format(tc+1, cost))
