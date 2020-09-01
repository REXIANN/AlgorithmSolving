# 1486.py 장훈이의 높은 선반
import sys
sys.stdin = open("1486input.txt", "r")

def bt(k, N, s=0):
    global maxV
    if s > maxV: return 
    if k == N:
        if s < B: return
        maxV = s if s < maxV else maxV
    else:
        bt(k+1, N, s)
        bt(k+1, N, s + H[k])

for tc in range(int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    maxV = sum(H)
    bt(0, N)
    print('#{} {}'.format(tc+1, maxV - B))

